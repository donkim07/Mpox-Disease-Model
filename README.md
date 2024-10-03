# Mpox-Disease-Model
=====================

## Table of Contents
-----------------

* [Introduction](#introduction)
* [Getting Started](#getting-started)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [Acknowledgments](#acknowledgments)

## Introduction
------------

Mpox-Disease-Model is a Streamlit application that simulates the transmission dynamics of Monkeypox (Mpox) in Equateur Province, Democratic Republic of the Congo. The model uses a SEIR framework to categorize the population into four compartments: Susceptible (S), Exposed (E), Infectious (I), and Recovered (R). The model also includes an additional compartment for Vaccinated individuals (V).

## Getting Started
---------------

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.8+
* Streamlit
* NumPy
* SciPy
* Matplotlib
* PIL

### Installation

1. Clone the repository using `git clone https://github.com/donkim07/Mpox-Disease-Model.git`
2. Install the required packages using `pip install -r requirements.txt`

### Usage

1. Run the application using `streamlit run app.py`
2. Select a page from the sidebar to view the introduction, model description, simulation, or conclusion.

## Contributing
------------

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments
------------

* Tanzania Data Lab(DLAB) have played a major role in the completion of this project.
* Ifakara health institute is another institution that helped in gathering the parameters and leading through out.

## Model Description
-----------------

The Mpox model is a SEIR model that categorizes the population into four compartments: Susceptible (S), Exposed (E), Infectious (I), and Recovered (R). The model also includes an additional compartment for Vaccinated individuals (V).

### Model Without Vaccination

The model without vaccination is governed by the following equations:

* dS/dt = π - βSI/N - μS
* dE/dt = βSI/N - (α + μ) E
* dI/dt = αE - (γ + δ + μ) I
* dR/dt = γI - μR

### Model With Vaccination

The model with vaccination is governed by the following equations:

* dS/dt = π - βSI/N - μS - vS
* dV/dt = vS - (1-e) βVI/N - μV
* dE/dt = βSI/N + (1-e) βVI/N - (α + μ) E
* dI/dt = αE - (γ + δ + μ) I
* dR/dt = γI – μR

## Simulation
------------

The simulation displays the dynamics of the Mpox outbreak with and without vaccination. The user can select the model parameters and view the simulation results.

## Conclusion
----------

The Mpox model is a useful tool for understanding the transmission dynamics of Monkeypox in Equateur Province, Democratic Republic of the Congo. The model can be used to evaluate the impact of vaccination and other interventions on the spread of the disease.
```
