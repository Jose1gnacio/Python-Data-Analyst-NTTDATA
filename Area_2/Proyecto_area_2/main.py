from mysql_operations import get_crime_data
from mongodb_operations import get_hospital_data

def main():
    crime_data = get_crime_data()
    hospital_data = get_hospital_data()
    
    print("Crime Data:", crime_data)
    print("Hospital Data:", hospital_data)

if __name__ == "__main__":
    main()