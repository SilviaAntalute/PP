import khttp.responses.Response

class CleanGetRequest: HTTPGet {
    var getRequest: GetRequest
    var parentalControlDisallow: List<String> = listOf("https://www.facebook.com","https://www.steam.com")

    constructor(g: GetRequest)
    {
        getRequest=g;
    }

    override fun getResponse(): Response? {
        if(parentalControlDisallow.contains(getRequest.genericReq.url)) {
            println("Acces denied!")
            return null
        }
        else
            return getRequest.getResponse()
    }
}