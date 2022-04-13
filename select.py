import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://igorborisov:@localhost:5432/hw2')
connection = engine.connect()


print(connection.execute(
    '''
    select name, year_date from album
    where year_date = 2018;
    ''').fetchall())

print(connection.execute(
    '''
    select name, length from track
    where length = (select max(length) from track)
    ''').fetchall())

print(connection.execute(
    '''
    select name from track
    where length >= 3.5;
    ''').fetchall())

print(connection.execute(
    '''
    select name from compilation
    where year_date between 2018 and 2020;
    ''').fetchall())

print(connection.execute(
    '''
    select name from artist
    where name not like '%% %%';
    ''').fetchall())

print(connection.execute(
    '''
    select name from album
    where name iLIKE '%%my%%';
    ''').fetchall())