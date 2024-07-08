#!/usr/bin/env python3

import sys
from yaml import load_all, dump, FullLoader

def main():
    content = ''
    for line in sys.stdin:
        content += line
    yaml_docs = load_all(content, Loader=FullLoader)
    for doc in yaml_docs:
        if 'kind' in doc and doc['kind'] == 'Deployment':
            pod_spec = doc['spec']['template']['spec']
            pod_spec['nodeSelector'] = {'nodeType': 'proxy'}
        print('---')
        print(dump(doc))

if __name__ == '__main__':
    main()
