import csv
import detect_types
import os

def get_postgres_type(s):
    if s=="str":
        return "CHARACTER VARYING"
    if s=="int":
        return "BIGINT"
    if s=="float":
        return "DOUBLE PRECISION"
    if s=="datetime":
        return "TIMESTAMP WITH TIME ZONE"

def make_postgres_schema(csv_path, table_name):
    reader = csv.reader(open(csv_path))
    columns = reader.next()
    try:
        types = [detect_types.detect_type(s) for s in reader.next()]
    except StopIteration:
        types = ["str" for s in columns]
    script_rows = ["CREATE TABLE %s (" % table_name]
    for col, t in zip(columns, types):
        script_rows.append("    %s %s," % (col, get_postgres_type(t)))
    script_rows[-1] = script_rows[-1][:-1] + ");"

    return "\n".join(script_rows)

def make_postgres_ingest(csv_path, table_name):
    return "COPY %s FROM '%s' DELIMITERS ',' CSV HEADER;" % (table_name, csv_path)

if __name__=="__main__":
    import os

    path = os.path.join(os.environ["DataPath"], "GEFlight", "Release 1", "InitialTrainingSet_rev1", "2012_11_17", "FlightHistory", "flighthistory.csv")
    script = make_postgres_script(path, "FlightHistory")

    f = open(os.path.join(os.environ["DataPath"], "GEFlight", "Postgres Scripts", "fh.sql"), "w")
    f.write(script)
    f.close()