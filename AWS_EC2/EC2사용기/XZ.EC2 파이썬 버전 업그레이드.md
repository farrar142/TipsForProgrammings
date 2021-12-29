sudo yum install gcc openssl-devel bzip2-devel libffi-devel -y
cd /opt
sudo wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
sudo tar -xvzf Python-3.8.0.tgz
cd Python*
sudo ./configure --enable-optimizations
sudo make altinstall


or

cd /usr/bin
ls | grep python

update-alternatives --install /bin/python2.7 python /bin/python3.7