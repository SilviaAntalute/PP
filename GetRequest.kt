import khttp.responses.Response

class GetRequest: HTTPGet {
    var timeout: Int
    var genericReq: GenericRequest

    constructor(u: String, p: MutableMap<String, String>?, t: Int){
        genericReq=GenericRequest(u,p).clone();
        timeout=t;
    }

    override fun getResponse():Response?{
        if(genericReq.params==null)
            return khttp.get(genericReq.url)
        else
            return khttp.get(genericReq.url, genericReq.params!!);
    }
}