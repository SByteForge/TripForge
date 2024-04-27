# Taxi Trip Analysis Project

This project aims to analyze a dataset containing details of taxi trips conducted by a taxi trip company. The dataset includes information such as trip duration, trip distance, fare amount, pickup location, drop-off location, and various other attributes related to each trip.

## Dataset Description

The dataset consists of the following columns:

- `hvfhs_license_num`: License number of the taxi driver
- `dispatching_base_num`: Dispatching base number
- `originating_base_num`: Originating base number
- `request_datetime`: Date and time when the trip was requested
- `on_scene_datetime`: Date and time when the taxi arrived at the pickup location
- `pickup_datetime`: Date and time when the passenger(s) were picked up
- `dropoff_datetime`: Date and time when the passenger(s) were dropped off
- `PULocationID`: Pickup location identifier
- `DOLocationID`: Drop-off location identifier
- `trip_miles`: Distance traveled during the trip (in miles)
- `trip_time`: Duration of the trip (in seconds)
- `base_passenger_fare`: Base fare for the trip
- `tolls`: Tolls paid during the trip
- `bcf`: Base congestion fee
- `sales_tax`: Sales tax
- `congestion_surcharge`: Surcharge for congestion
- `airport_fee`: Airport fee
- `tips`: Tips received by the driver
- `driver_pay`: Amount paid to the driver
- `shared_request_flag`: Flag indicating whether the trip was shared
- `shared_match_flag`: Flag indicating whether the shared trip was matched
- `access_a_ride_flag`: Flag indicating whether the trip was for access-a-ride service
- `wav_request_flag`: Flag indicating whether the trip was requested via WAV (wheelchair accessible vehicle)
- `wav_match_flag`: Flag indicating whether the WAV request was matched

## Hypotheses Testing

Several hypotheses can be tested using this dataset, including:

1. Effect of Pickup Location on Trip Fare
2. Impact of Time of Day on Trip Duration
3. Association between Trip Miles and Trip Fare
4. Effect of Shared Request on Trip Tips
5. Impact of Congestion Surcharge on Trip Distance

## How to Use

1. Clone the repository:

        git clone <repository_url>

2. Install the required dependencies:

        pip install pyspark


3. Run the analysis scripts:

        python analyze.py



## Conclusion

This README provides an overview of the Taxi Trip Analysis Project, including the dataset description, hypotheses testing, and instructions for running the analysis scripts. For more detailed insights and results, refer to the analysis output and accompanying documentation.
