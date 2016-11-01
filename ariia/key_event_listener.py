# -*- coding: utf-8 -*-

from threading import Thread


class KeyEventListener(Thread):
    """
    Class listening to the key events
    """


    def __init__(self):
        """
        Constructor
        """

        Thread.__init__(self)
        self.checkLoop = True
        self.keyEvent  = False

        self.start()



    def unregisterListener(self):
        """
        Stops the checkloop
        """

        self.join()


    def waitKeyEvent(self):
        """
        Freeze the program until enter is pressed,
        this method has to be used in a loop
        """

        while not self.keyEvent:
            pass

        self.keyEvent = False



    def run(self):
        """
        The key event checkloop
        """

        while self.checkLoop:
            
            try:
                raw_input()

            except EOFError:
                self.checkLoop = False

            self.keyEvent = True