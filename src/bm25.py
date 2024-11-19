from math import log

from util import avgDocLen, numDocs


class BM25F:
    k1 = 1.5
    features = {
        'title': {'b': 0.75, 'v': 0.25, 'w': 0.25}, 
        'description': {'b': 0.75, 'v': 0.25, 'w': 0.25},
        'tags': {'b': 0.75, 'v': 0.25, 'w': 0.25},
        'body': {'b': 0.75, 'v': 0.25, 'w': 0.25}
    }


    def __init__(self):
        return

    def getDocTermFreq(self, d, q):
        """
        Get term frequency from terms in query for 
        all textual features in a document.
        """
        tfs = {'title': [], 'description': [], 'tags': [], 'body': []}

        for f in tfs.keys():
            for t in q:
                if t in d[f]:
                    tf = {t: 0}
                    for c,w in enumerate(d[f]):
                        if w == t:
                            tf[t] += 1
                    
                    if tf[t] > 0:
                        tf[t] = 1 + log(tf[t])

                    tfs[f].append(tf)

        return tfs

    
    def getDocFreq(self, d, t):
        df = 0
        for w in d['body']:
            if w == t:
                df += 1

        return df


    def normalizeTFs(self, tfs, d, q):
        """
        Normalize the term frequencies for each feature
        """
        r = {}
        for w in q:
            tfnorm = 0
            for zone in self.features.keys():
                avdl = avgDocLen(zone, self.features[zone]['w'])
                B = (1-self.features[zone]['b']) + self.features[zone]['b'] * (len(d['title']) * self.features[zone]['w'] / avdl)
                
                for t in tfs[zone]:
                    if list(t.keys())[0] == w:
                        tf = t[list(t.keys())[0]]
                        tf = self.features[zone]['v'] * (tf / B)
                        tfnorm += tf

            r[w] = tfnorm

        return r

    
    def score(self, ntf, d, q):
        s = 0
        for w in q:
            df = self.getDocFreq(d, w)
            if df > 0:
                s += log(numDocs()/df) * (((self.k1 + 1) * ntf[w]) / self.k1 + ntf[w])

        return s
