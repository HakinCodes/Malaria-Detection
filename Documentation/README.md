# TensorFlow Documentation
<div align="center">
  <img src="https://www.tensorflow.org/images/tf_logo_horizontal.png"><br><br>
</div>

## About Tensorflow
**TensorFlow** is an open source machine learning framework owned and maintained by Google. It is used for implementing machine learning and deep learning applications.

It combines the computational algebra of optimization techniques for easy calculation of many mathematical expressions.<br>

<br>

### Some features of TensorFlow −

- It includes a feature of that defines, optimizes and calculates mathematical expressions easily with the help of multi-dimensional arrays called tensors.

- It includes a programming support of deep neural networks and machine learning techniques.

- It includes a high scalable feature of computation with various data sets.

- TensorFlow uses GPU computing, automating management. It also includes a unique feature of optimization of same memory and the data used.

<br>
<br>

## Installation

**Before installing tensorflow some tools like Anaconda, Python are needed to be installed.**

1. First of all lets download and install Anaconda which is a python distribution service.

2. According to your Operating System, Select and download from the provided link.
- [ Windows (64bit) ](https://repo.anaconda.com/archive/Anaconda3-2020.07-Windows-x86_64.exe) 
- [ Windows (32bit) ](https://repo.anaconda.com/archive/Anaconda3-2020.07-Windows-x86.exe)
- [Mac Graphic installer](https://repo.anaconda.com/archive/Anaconda3-2020.07-MacOSX-x86_64.pkg)
- [Mac Command line installer](https://repo.anaconda.com/archive/Anaconda3-2020.07-MacOSX-x86_64.sh)
- [Linux(x86)](https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh)
- [Linux (power8 and power9)](https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-ppc64le.sh)
- You can go to official website for the same.[Anaconda](https://www.anaconda.com/products/individual)

3. After downloading above, install the same on your system.

4. Anaconda provide us most of the tools required to run tensorflow including python,pip and other python modules.

5. Now our ystem is ready to install tensorflow.

**Installing Tesnorflow**

1. Check your python and pip version using bellow commands one by one.

        python --version
        pip --version

    In the terminal you should get something like :

        python 3.x.x  
        pip 20.x.x

        
2. To install tensorflow run the following command

        pip3 install --user --upgrade tensorflow  # install in $HOME

    Installation will take time and if asked something like y/n then press y.
  
3. To check if the installation of tensorflow is successful or not run following commands one by one in terminal/cmd.

        python
        import tensorflow as tf
        tf.version

    you should get something(not compulsory to be exact same) like -
     <module 'tensorflow._api.v2.version' from'C:\\ Users \\ xxxxxxxxx \ xxxxxxx>

<br>
<br>

#### If you face any issues you can look up into official documentation [here](https://www.tensorflow.org/install/pip)

        
  



