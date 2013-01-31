import csv
import detect_types
import os

def get_postgres_type(s):
    if s=="str":
        return "character varying"
    if s=="int":
        return "bigint"
    if s=="float":
        return "double precision"
    if s=="datetime":
        return "timestamp with time zone"

def make_postgres_script(csv_path, table_name):
    reader = csv.reader(open(csv_path))
    columns = reader.next()
    types = [detect_types.detect_type(s) for s in reader.next()]
    script_rows = ["CREATE TABLE %s (" % table_name]
    for col, t in zip(columns, types):
        script_rows.append("    %s %s," % (col, get_postgres_type(t)))
    script_rows[-1] = script_rows[-1][:-1] + ");"
    script_rows.append("")
    script_rows.append("COPY %s FROM '%s' DELIMITERS ',' CSV;" % (table_name, csv_path))

    return "\n".join(script_rows)

if __name__=="__main__":
    import os

    path = os.path.join(os.environ["DataPath"], "GEFlight", "Release 1", "InitialTrainingSet_rev1", "2012_11_17", "FlightHistory", "flighthistory.csv")
    script = make_postgres_script(path, "FlightHistory")

    f = open(os.path.join(os.environ["DataPath"], "GEFlight", "Postgres Scripts", "fh.sql"), "w")
    f.write(script)
    f.close()