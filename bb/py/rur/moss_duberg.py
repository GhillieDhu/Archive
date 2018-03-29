import sys
from homunculus import homunculus

class moss_duberg(homunculus):

    def open_moss_duberg(self):
        self.sequence('moss-duberg-open.hom')

    def load_library(self):
        self.sequence('moss-duberg-load-library.hom')

    def save_mossout(self):
        self.sequence('moss-duberg-save-mossout.hom')

    def exit_moss_duberg(self):
        self.sequence('moss-duberg-exit.hom')

if __name__ == '__main__':
    md = moss_duberg()
    md.library = sys.argv[1]
    md.mossout = sys.argv[2]
    md.open_moss_duberg()
    md.load_library()
    md.save_mossout()
    md.exit_moss_duberg()