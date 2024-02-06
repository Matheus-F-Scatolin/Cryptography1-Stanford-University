import urllib.request as urllib1
import urllib.error as urllib2

TARGET = 'http://crypto-class.appspot.com/po?er='
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib1.quote(q)    # Create query URL
        target = urllib1.unquote(target)      # URL decode the target
        try:
            f = urllib1.urlopen(target)          # Wait for response
        except urllib2.HTTPError as e:
            print(f"{q[94:96]}: {e.code}")       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding