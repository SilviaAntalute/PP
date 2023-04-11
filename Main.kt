import java.io.File
import java.sql.Timestamp
import java.text.SimpleDateFormat
import java.util.*
interface Comparable<in T> {
    operator fun compareTo(other: T): Int
}

data class HistoryLogRecord(val timestamp:Date, val CommandLine:String,val Upgrade:String,val End_date:String):Comparable<HistoryLogRecord>{
    override fun compareTo(other:HistoryLogRecord):Int{
        return this.timestamp.compareTo(other.timestamp)
    }
}
fun <T:Comparable<T>>max(first: T,second:T):T{
    val k=first.compareTo(second)
    return if(k>=0) first else second
}
fun isEqual(v1: HistoryLogRecord,v2: HistoryLogRecord):Boolean{
    if (v1.timestamp.equals(v2.timestamp)&&v1.CommandLine.equals(v2.CommandLine)&&v1.Upgrade.equals(v2.Upgrade)&&v1.End_date.equals(v2.End_date))
        return true
    else
        return false
}
//fun findAndReplace(target:HistoryLogRecord,objReplace:HistoryLogRecord,map:MutableMap<out Date,HistoryLogRecord>){
//    for(key in map.keys.toList()) {
//        val valoare: HistoryLogRecord = map.getValue(key)
//        if(isEqual(valoare,target) )
//        {
//            map.remove(key)
//            map.plusAssign(key to objReplace)
//        }
//    }
//}
fun main(args: Array<String>) {
    val file = File("/var/log/apt/history.log")
    val scanner = Scanner(file)
    val format = SimpleDateFormat(" yyyy-MM-dd  HH:mm:ss")
    scanner.nextLine()
    var map: MutableMap<Date, HistoryLogRecord> = mutableMapOf()
    while (scanner.hasNext()) {
        val timestamp = format.parse(scanner.nextLine().removePrefix("Start-Date:"))
        val CommandLine = scanner.nextLine().removePrefix("CommandLine:")
        val upgrade = scanner.nextLine().removePrefix("Upgrade:")
        val end_date = scanner.nextLine().removePrefix("End-Date:")
        if (scanner.hasNext())
            scanner.nextLine()
        map.plusAssign(timestamp to HistoryLogRecord(timestamp, CommandLine, upgrade, end_date))
    }
    map.forEach { (_,value) -> println(value)
    println()}

    println("Obiectul cu data mai recenta dintre primul si al doilea: ")
    println(max(map.values.elementAt(0),map.values.elementAt(1)))
}