from setuptools import setup
import setup_translate

pkg = 'Extensions.SRFMediathek'
setup(name='enigma2-plugin-extensions-srfmediathek',
       version='3.0',
       description='Zugriff auf die SRF-Mediathek',
       package_dir={pkg: 'SRFMediathek'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'logo.png', 'maintainer.info', 'skin_FHD.xml', 'skin_HD.xml', 'img/*.png']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
