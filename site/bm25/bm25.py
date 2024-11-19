from math import log

from util import avgDocLen, numDocs


class BM25F:
    k1 = 1.5
    features = {
        'title': {'b': 0.75, 'v': 0.25, 'w': 0.25},
        'description': {'b': 0.75, 'v': 0.25, 'w': 0.25},
        'tags': {'b': 0.75, 'v': 0.25, 'w': 0.25},
        'body': {'b': 0.75, 'v': 0.25, 'w': 0.25},
    }

    @staticmethod
    def getDocTermFreq(d, q):
        tfs = {'title': [], 'description': [], 'tags': [], 'body': []}

        for f in tfs.keys():
            for t in q:
                if t in d[f]:
                    tf = {t: 0}
                    for c, w in enumerate(d[f]):
                        if w == t:
                            tf[t] += 1

                    if tf[t] > 0:
                        tf[t] = 1 + log(tf[t])

                    tfs[f].append(tf)

        return tfs

    @staticmethod
    def getDocFreq(d, t):
        df = 0
        for w in d['body']:
            if w == t:
                df += 1

        return df

    @staticmethod
    def normalizeTFs(tfs, d, q):
        r = {}
        for w in q:
            tfnorm = 0
            for zone in BM25F.features.keys():
                avdl = avgDocLen(zone, BM25F.features[zone]['w'])
                B = (1-BM25F.features[zone]['b']) + BM25F.features[zone]['b'] * (len(d['title']) * BM25F.features[zone]['w'] / avdl)

                for t in tfs[zone]:
                    if list(t.keys())[0] == w:
                        tf = t[list(t.keys())[0]]
                        tf = BM25F.features[zone]['v'] * (tf / B)
                        tfnorm += tf

            r[w] = tfnorm

        return r

    @staticmethod
    def score(ntf, d, q):
        s = 0
        for w in q:
            df = BM25F.getDocFreq(d, w)
            if df > 0:
                s += log(numDocs()/df) * (((BM25F.k1 + 1) * ntf[w]) / BM25F.k1 + ntf[w])

        return s
