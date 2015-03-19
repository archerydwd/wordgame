# wordgame
python wordgame on OVH vps tutorial

=
###Set up git repo

I created a new git repo on github.com and followed the provided instructions to initialise my wordgame application folder as a git repo.

=
###Set up OVH vps

Go to https://www.ovh.ie/vps/vps-classic.xml and order the VPS Classic 1 for €2.

* Under the My VPS heading you can leave the settings as they are.
* Under the My Location heading select Europe Roubaix which is the closest location to Ireland.
* Under the My OS heading change the distribution to Ubuntu and the version to Ubuntu 14.10 Server 64bits and the language to English.

Continue with the order. Once done you will be provided with a link to the page to view your server and an ip address.

=
###Install Python

At time of writing this the Python version was: 3.4.3 and the Flask version was: 0.10.1

```
wget http://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz
tar -xzf Python-3.4.3.tgz  
cd Python-3.4.3

./configure  
make  
sudo make install
```

=
###Install pip

We will use pip to install flask.

```
sudo apt-get install python-pip
```

=
###Install Flask

```
sudo pip install Flask
```

=
###Get Wordgame on the server

issue the following command, replacing my ip address with yours:

```
ssh root@46.105.16.62
```

change directory to var/www/

install git

Then issue the following command:

```
git clone https://github.com/archerydwd/wordgame.git
```

=
###Install Apache & Vim

Open a terminal and enter the following commands:

```
sudo apt-get upgrade
sudo apt-get update
sudo apt-get install apache2
sudo apt-get install vim        //or your favourite text editor
```

=
###Install and Enable Mod_wsgi

Mod_wsgi is an interface between web servers and python web applications. It is an Apache HTTP server mod that enables Apache to serve Flask applications.

**Install**

```
sudo apt-get install libapache2-mod-wsgi python-dev
```

**Enable**

```
sudo a2enmod wsgi
```

=
###Changes to the app structure

We are going to make a few changes to this application:

Inside the /var/www/wordgame/ directory, do:

```
mkdir wordgame
mv * wordgame/
touch wordgame.wsgi
cd wordgame/
mv wordgameapp.py __init__.py
```


