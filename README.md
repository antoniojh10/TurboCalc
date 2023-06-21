# Pump Parameters Calculation

This repository provides a collection of scripts and tools for calculating the parameters of a centrifugal pump. The calculations are based on various formulas and equations (mainly obtained from the book "Centrifugal Pumps", Gulich - 2010) commonly used in fluid mechanics and pump engineering. By utilizing these tools, users can obtain a first approximation to desing and then simulate and test an impeller and its volute.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Available Calculations](#available-calculations)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Centrifugal pumps are widely used in various industries to transport fluids. To analyze and optimize the performance of a centrifugal pump, it is essential to accurately determine its parameters. This repository aims to provide a convenient and efficient way to calculate the geometry of the pump with the following input parameters:

1. Flow rate (Q) - the volume of fluid passing through the pump per unit of time.
2. Total head (H) - the total energy imparted to the fluid by the pump per unit of weight.
3. Rotational speed (n) - the impeller rotational speed in RPM.

## Installation

To use the calculation scripts and tools provided in this repository, please follow these steps:

1. Clone the repository to your local machine using the following command:

```shell
git clone https://github.com/antoniojh10/TurboCalc
```

2. Navigate to the cloned directory:

```shell
cd TurboCalc
```

3. Install the required dependencies:

```shell
pip install -r requirements.txt
```

4. You're ready to use the pump parameter calculation tools!

## Usage

Follow the instructions provided in its respective directory:

```shell
python3 main.py
```

## Contributing

Contributions to this repository are welcome. If you have any improvements, bug fixes, or additional calculations to contribute, please follow the standard GitHub workflow:

1. Fork the repository.
2. Create a new branch for your feature/fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request explaining your changes.

Thank you for your contributions!
