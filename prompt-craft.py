#!/usr/bin/env python3
import sys
import os
from random import randint

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog
)

from PyQt5.uic import loadUi
from main_window_ui import Ui_MainWindow

TXT2IMG_STR = 'txt2img'
IMG2IMG_STR = 'img2img'
MODES = [TXT2IMG_STR, IMG2IMG_STR]
PREC_FULL = 'full'
PREC_AUTO = 'autocast'
PRECISION = [ PREC_FULL, PREC_AUTO ]


class Window( QMainWindow, Ui_MainWindow ):
    def __init__( self, parent = None ):
        super().__init__(parent)
        self.setupUi(self)
        self.modeSetup()
        self.precisionSetup()
        self.connectSignalsSlots()

        # Set widget states (allows designer to change)
        self.setSeedEnabled()

    def modeSetup(self):
        self.modeBox.addItems( MODES )
        self.modeBox.activated.connect( self.mode_update )
        self.toggle_mode()
        
    def precisionSetup(self):
        self.precisionBox.addItems( PRECISION )
        
    def connectSignalsSlots(self):
        self.actionExit.triggered.connect(self.close)
        self.actionRun.triggered.connect(self.run_prompt)
        self.actionAbout.triggered.connect(self.about)

    def mode_update( self ):
        mode       = self.modeBox.currentText()
        print( 'mode updated to: {} '.format(  mode ) )

    def setSeedEnabled( self ):
        rand_seed = self.rand_seed.isChecked()
        use_seed  = self.use_seed.isChecked()        
        self.seed.setEnabled( ( not rand_seed ) and use_seed )
        self.rand_seed.setEnabled( use_seed )
    
    def toggle_rand_seed( self ):
        self.setSeedEnabled()

    def toggle_use_seed( self ):
        self.setSeedEnabled()

    def toggle_mode( self ):
        mode = self.modeBox.currentIndex()
        self.plms.setEnabled( mode == 0 )
        self.height.setEnabled( mode == 0 )
        self.width.setEnabled( mode == 0 )
        self.init_img.setEnabled( mode == 1 )
        self.input_browse.setEnabled( mode == 1 )
        self.strength.setEnabled( mode == 1 )
        

    def init_image_dialog( self ):
        start = os.path.expanduser( '~/Pictures' )
        fname = QFileDialog.getOpenFileName( self, 'init-img', start )[0]
        self.init_img.setText( fname )

    def outdir_dialog( self ):
        path = QFileDialog.getExistingDirectory( self, 'outdir', 'All Directories' )
        self.outdir.setText( path )
    
    def run_prompt(self):
        print( 'working' )
        prompt     = self.prompt.toPlainText()
        n_samples  = self.n_samples.value()
        n_iter     = self.n_iter.value()
        strength   = self.strength.value()
        ddim_eta   = self.ddim_eta.value()
        ddim_step  = self.ddim_step.value()
        plms       = self.plms.isChecked()
        seed       = self.seed.value()
        rand_seed  = self.rand_seed.isChecked()
        use_seed   = self.use_seed.isChecked()

        if rand_seed:
            seed = randint(0, 4294967295 )
        
        init_image = self.init_img.text()
        # Unsure if this will be needed...
        # if init_image.startswith('~'):
        #     init_image = os.path.expanduser( init_image )
            
        outdir     = self.outdir.text()
        mode       = self.modeBox.currentText()
        scripts    = { TXT2IMG_STR: 'scripts/txt2img.py',
                       IMG2IMG_STR: 'scripts/img2img.py'}
        script = scripts[mode]
        if not os.path.exists( script ):
            print( 'Script: {} not found'.format( script ) )

        height = self.height.value()
        width  = self.width.value()

        precision = self.precisionBox.currentText()

        # Construct the parts
        _script    = 'python {}'.format( script )
        _prompt    = ' --prompt "{}"'.format( prompt )
        _samples   = ' --n_samples {}'.format( n_samples )
        _n_iter    = ' --n_iter {}'.format( n_iter )
        _strength  = ' --strength {}'.format( strength )
        _height    = ' --H {}'.format( height )
        _width     = ' --W {}'.format( width )
        _plms      = ' --plsm'
        _ddim_eta  = ' --ddim_eta {}'.format( ddim_eta )
        _ddim_step = ' --ddim_step {}'.format( ddim_step )        
        _precision = ' --precision {}'.format( precision )
        _init_img  = ' --init-img {}'.format( init_image )
        _outdir    = ' --outdir {}'.format( outdir )
        _seed      = ' --seed {}'.format( seed )

        # Craft the command
        cmd = ''
        cmd += _script
        cmd += _prompt
        cmd += _samples
        cmd += _n_iter

        # TODO
        #cmd += _ddim_eta
        #cmd += _ddim_step
        #cmd += _precision
        #cmd += _outdir
        
        # txt2img options
        if mode == TXT2IMG_STR:
            cmd += _height
            cmd += _width

        # img2txt options
        if mode == IMG2IMG_STR:
            cmd += _strength
            cmd += _init_img

        if use_seed:
            cmd += _seed
        
        execute = cmd
        
        # cmd = 'python {} --prompt "{}" --n_samples {} --n_iter {} --init-img {} --strength {}'
        # execute = cmd.format( script, prompt, n_samples, n_iter, init_image, strength )
        print( execute )
        os.system( execute )

    def about(self):
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )

class FindReplaceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/find_replace.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
