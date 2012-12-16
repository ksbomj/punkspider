import sys
import os
import subprocess
cwdir = os.path.dirname(__file__)
punkscan_base = os.path.join(cwdir, "../")
sys.path.append(os.path.join(punkscan_base,"pysolr/"))
from ConfigParser import SafeConfigParser
config_parser = SafeConfigParser()
config_parser.read(os.path.join(punkscan_base,'punkscan_configs', 'punkscan_config.cfg'))
HADOOP_HOME=config_parser.get('directories','HADOOP_HOME')
NUTCH_HOME=config_parser.get('directories','NUTCH_HOME')
NUTCH_RUNTIME_DEP = os.path.join(NUTCH_HOME, "runtime", "deploy")

class NutchController:

	def crawl(self):

		topN = config_parser.get('performance','topN')
		depth = config_parser.get('performance','depth')
		nutch_bin = os.path.join('bin', 'nutch')
		if topN.lower() == "all":
			shell_call_list = [nutch_bin, "crawl", "urls", "-dir", "punkscan_crawl", "-depth", depth]
		else:
			shell_call_list = [nutch_bin, "crawl", "urls", "-dir", "punkscan_crawl", "-depth", depth, "-topN", topN]

		output = subprocess.Popen(shell_call_list, cwd = NUTCH_RUNTIME_DEP).communicate()[0]

if __name__ == "__main__":

	NutchController().crawl()