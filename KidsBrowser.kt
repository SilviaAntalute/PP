import java.util.*

class KidsBrowser {
    lateinit var cleanGet: CleanGetRequest
    lateinit var postReq: PostRequest

    fun start()
    {
        val input = Scanner(System.`in`)
        var task=1
        print("0 - Exit\n1 - Get\n2 - Post\nEnter task: ")
        task = input.nextInt()
        while(task!=0) {
            if(task==1) {

                var url = ""
                print("Enter URL: ")
                url = readLine()!!
                cleanGet = CleanGetRequest(GetRequest("https://$url", null, 5))
                var response = cleanGet.getResponse()
                if (response != null) {
                    println("Response: " + response.url)
                }

            }
            else if(task==2) {
                var url = ""
                var param1 = ""
                var param2 = ""
                print("Enter URL: ")
                url = readLine()!!
                print("Enter Params: ")
                param1 = readLine()!!
                param1 = readLine()!!
                postReq = PostRequest("https://$url", mutableMapOf(param1 to param2))
                var response = postReq!!.postData()
                if (response != null) {
                    println("Response: " + response.url)
                }

            }
            else
                println("Unknown task.")
            print("0 - Exit\n1 - Get\n2 - Post\nEnter task: ")
            task = input.nextInt()
        }
    }
}
