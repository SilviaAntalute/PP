import khttp.responses.Response

class PostRequest {
    var genericReq: GenericRequest

    constructor(u: String, p: MutableMap<String, String>){
        genericReq=GenericRequest(u,p).clone();
    }

    fun postData(): Response? {
        return genericReq.params?.let { khttp.post(genericReq.url, it) }
    }
}