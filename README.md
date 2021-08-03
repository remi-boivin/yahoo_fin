<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Scalnyx/SP-500">
    <img src="datas/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">SPNANI</h3>

  <p align="center">
    Scrap all stock exchange's datas.
    <br />
    <a href="https://github.com/Scalnyx/SP-500/issues">Report Bug </a>
    ·
    <a href="https://github.com/Scalnyx/SP-500/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

* Create a virtualenv
  ```sh
  python3 -m venv VIRTUALENV_NAME
  ```
  * source the virtualenv
  ```sh
  source MY_DIR/VIRTUALENV_NAME/bin/activate
  ```
  You need to replace MY_DIR/ by the VIRTUALENV_NAME path and VIRTUALENV_NAME by the name of your virtualenv


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Scalnyx/SP-500.git
   ```
2. Install dependencies
   ```sh
   pip3 install -r requirements.txt
   ```

## Usage

  ```sh
 python3 scrap.py -h
 ```

Print the help message

  ```sh
 python3 scrap.py -s SP-500 -d 2020/08/03
 ```

you will recover sp-500 stock exchange datas

## Stock exchange list
* NASDAQ
* FTSE
* SP-500
* NIFTY
* OTHER

## Contact

Project Link: [https://github.com/Scalnyx/SP-500](https://github.com/Scalnyx/SP-500)
