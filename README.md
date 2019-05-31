# Sensor Gateway Simulator

Software for simulate the operation of a sensor

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
Python
```

### Installing

1. Install npm project dependecies

```
npm install
```

## Deployment

1. Set environments variables

```
BROKER_URL // the url of the mqtt broker
BROKER_PORT // the port of the mqtt broker
TOPIC // the topic in which you listen
DEVICE_ID // the ID of the device that sends the data
LATITUDE // the latitude of the device position
LONGITUDE // the longitude of the device position
```

2. Run the gateway simulator

```
python src/gateway.py
```

## Built With

* [Python](https://www.python.org/)

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details
