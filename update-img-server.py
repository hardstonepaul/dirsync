#actulaizar carpetas imagenes
#esferos
#/home/g0esferos/public_html/site/img/p
#catalogo
#/home/c4t4l0g0esp/public_html/img/p

from dirsync import sync
esferos = '/home/g0esferos/public_html/site/img/p'
catalogo = '/home/c4t4l0g0esp/public_html/img/p'
sync(esferos, catalogo, 'sync', purge = True)


#----- to restore folder permissions
#sudo chmod 755 -R /home/c4t4l0g0esp/public_html/img
#sudo chmod 755 -R /home/iejj8sumklhb/public_html/img

# put all folders in a 755
#find /opt/lampp/htdocs -type d -exec chmod 755 {} \;
