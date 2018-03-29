import sys
from homunculus import homunculus

class feadms(homunculus):

    def open_feadms(self):
        self.sequence('feadms-open.hom')

    def load_model(self):
        self.sequence('feadms-load-model.hom')

    def filter_loads(self):
        self.sequence('feadms-filter-loads.hom')

    def switch_grs(self):
        self.sequence('feadms-switch-to-grs.hom')

    def load_detail(self):
        self.sequence('feadms-load-detail.hom')

    def load_settings(self):
        self.sequence('feadms-load-settings.hom')

    def export_data(self):
        self.sequence('feadms-export-data.hom')

    def switch_feadms(self):
        self.sequence('feadms-switch-from-grs.hom')

    def exit_feadms(self):
        self.sequence('feadms-exit.hom')

if __name__ == '__main__':
    f = feadms()
    f.modelnumber = sys.argv[1]
    f.loadfilter = sys.argv[2]
    f.settings = sys.argv[3]
    f.detailfile = sys.argv[4]
    f.datfile = sys.argv[5]
    f.open_feadms()
    f.load_model()
    f.filter_loads()
    f.switch_grs()
    f.load_detail()
    f.switch_feadms()
    f.load_settings()
    f.export_data()
    f.exit_feadms()