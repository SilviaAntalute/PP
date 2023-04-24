open class GenericRequest: Cloneable {
    var url: String=""
    var params: MutableMap<String, String>?

    constructor(u: String, p: MutableMap<String, String>?){
        url=u;
        params=p;
    }

    public override fun clone():GenericRequest{
        return GenericRequest(url, params)
    }
}