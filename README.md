# Halloween, Jägerbomber costume

a costume with a raspberry pi on battery with a 4Digit 7 segments display that shows a countdown

# Installing

	apt-get install raspi-copies-and-fills python i2c-tools python-smbus 
	echo "i2c-dev" >> /etc/modules
	
	ln -fs `pwd`/start.sh /etc/init.d/python_clock
	update-rc.d python_clock defaults
	
# Sources

https://github.com/debian-pi/raspbian-ua-netinst
http://skpang.co.uk/blog/archives/575
http://razzpisampler.oreilly.com/ch09.html