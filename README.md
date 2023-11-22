# Introductory Python Data Manipulation Project

This is an introductory project in python to understand the basics of manipulating data in Python and uploading the data to MySQL workbench. The project utilizes the libraries - pandas (for manipulating and analyzing data, pandas has data structures like DataFrames for efficient handling and examination of tabular data), matplotlib.pyplot and sqlalchemy (libraries is used to create static, animated, and interactive visualizations) and pymysql (A Python MySQL database adapter facilitating communication between Python applications and MySQL databases).

## Getting Started

The following instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system:

### Prerequisites

Following softwares and sample dataset are necessary to run the project:

1. Anaconda Navigator
2. MySQL Workbench
3. Dataset - Data of the top youtube channels from the website https://socialblade.com/youtube/

### Installing

Installing Anaconda Navigator and Starting Jupyter Notebooks

1. Visit the Anaconda website and download the appropriate version for your operating system (Windows, macOS, or Linux).
2. Locate the installation file in your downloads folder and follow the installation instructions for your operating system. Anaconda Navigator is included in the Anaconda distribution.
3. Once installed, open Anaconda Navigator. You can find it in your applications or programs menu.
4. In Anaconda Navigator, find and launch Jupyter Notebook from the Navigator's home screen.
5. Once Jupyter Notebook is open in your web browser, click on the "New" button and select "Python 3" to create a new Python notebook.

Installing MySQL workbench:

1. Visit the MySQL website and download the MySQL workbench (https://dev.mysql.com/downloads/windows/installer/8.0.html).
2. Locate the installation file in downloads in run the installer (.exe) file by double-clicking on it.
3. Follow the on-screen instructions to complete the MySQL Workbench installation.
4. Detailed instructions can be found here - https://www.mysqltutorial.org/install-mysql/
5. Set up the password and create a user proile to connect and execute MySQL workbench queries from python.

## Running the tests

Data of the top youtube channels is obtained from the website https://socialblade.com/youtube/
This data is loaded into the Juypter Notebook environment

### Break down into end to end tests

1. The dataset ‘youtube_dataset.csv’ is read into a DataFrame
2. After the data is loaded, we perform certain validation steps to check the loaded DataFrame. This is done by utilizing methods and attributes such as .head(), .tail(), .shape, and .dtypes.
.head() is a method that returns the first few rows of a DataFrame
.tail() is a method that returns the last few rows of a DataFrame
.shape is an attribute that gives the number of rows and columns in a DataFrame
.dtypes is an attribute that shows the data types of each column in a DataFrame
3. Using the function dist_channel_1000records we calculate and diplay the distribution of top 1000 youtube channels.
4. Using the function function plot_distribution we plot the distribution of the top 1000 youtube channels.
5. We create a csv file of the records of top 1000 youtube channels and then load the data into a dataframe and then using the .to_sql() method, contents the of python dataframe are loaded into MySQL workbench.
6. We then check the MySQL workbench. A select query shows that all the records 1000 have been loaded into the MySQL table.


## Deployment

1. The Jupyter Notebook is uploaded in this repository, which can be viewed and downloaded.
2. Once downloaded, open Anaconda Navigator, launch Jupyter Notebook.
3. The code in the Jupyter Notebook can be copied or the notebook can be direclty uploaded into the environment.
4. The comments and helpful headings in markdown languange within Jupyter notebook help with necessary changes.
5. The location of the dataset has to be specified in the pd.read_csv() method.
6. In MySQL workbench a user account has to be created with appropriate access control, which can be used for establishing connection.
7. When establishing the connection between Python and MySQL workbench connection string, the username and Password, the connection IP address, and the database name along with the connection parameter ‘mysql+pymysql’ have to be passed to the 'create_engine' function.

## Built With

* [Anacoda Navigator 2.4.3 - Jupyter Notebook 6.5.4](https://www.anaconda.com/download) - Code in Python
* [MySQL Workbench 8.0.35](https://dev.mysql.com/downloads/windows/installer/8.0.html) - Database to store the results

## Authors

* Narahara Karthik L - [Karthiklnk](https://github.com/Karthiklnk)
* Pavan Kumar Valluri - [https://in.linkedin.com/in/valluri-pavan-kumar-b96702127]

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

### Many thanks and great acknowledgments to Professor Omar Al-Trad, Ph.D.
