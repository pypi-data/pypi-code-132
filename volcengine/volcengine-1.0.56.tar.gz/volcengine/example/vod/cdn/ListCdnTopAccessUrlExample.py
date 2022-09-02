# coding:utf-8
from __future__ import print_function

from volcengine.vod.VodService import VodService
from volcengine.vod.models.request.request_vod_pb2 import VodListCdnTopAccessUrlRequest

if __name__ == '__main__':
    vod_service = VodService()
    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    vod_service.set_ak('your ak')
    vod_service.set_sk('your sk')
    try:
        req = VodListCdnTopAccessUrlRequest()
        req.Domains = 'your domian'
        req.StartTimestamp = 0
        req.EndTimestamp = 0
        req.SortType = 'your sort type'
        resp = vod_service.list_cdn_top_access_url(req)
    except Exception:
        raise
    else:
        print(resp)
        if resp.ResponseMetadata.Error.Code != '':
            print(resp.ResponseMetadata.Error)
