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

# put all folders in a 755
#find /home/c4t4l0g0esp/public_html/img -type d -exec chmod 755 {} \;

#----- to restore folder owner
# sudo chown -R c4t4l0g0esp:c4t4l0g0esp /home/c4t4l0g0esp/public_html/img
