# RandomNum
Creates random number using weather data


## How to use
1. Download and run python file locally (Note some libraries might need to be installed)
2. REQUEST DATA: Send a HTTP GET request to http://127.0.0.1:5000/getRand (Can be done with a Python library or an application like Postman)
3. RECEIVE DATA: JSON output, looks like:
    {
        "RandomNum": 0.18720655959119203,
        "Seed": 10846502327
    }

## How it works
This microservice can conceptually be split into 3 components:
1. Getting "randomness" from real world weather data
2. Getting "randomness" from local hardware entropy
3. Tumbling both generated values to create a random seed in which to create a pseudorandom number from

Firstly the program generates a number between 1-100 from hardware entropy and uses this number to be the number of weather data points that will be collected. The program then generates another random number from hardware entropy for the number of desired weather data points. At each weather data point, a real world based random number is generated by combining the wind speed, wind direction, and current temperature of a real world location. This combined value generated at the weather data point is than scaled by another entropy generated random number and accumulated until the loop ends. Finally a random seed is generated and called upon to create a random float between 0:1.

![Sequence diagram](https://github.com/StruggleWuggle/RandomNum/assets/87583779/dc196302-a9c1-4670-a43a-8f8d1b2a6482)

## Communication contract
send HTTPS GET request using http://127.0.0.1:5000/getRand, receive a JSON file containing the seed and a random num between 0 and 1



