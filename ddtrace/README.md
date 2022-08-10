# Usage

1. Find the /api/v1/trace/ responce in the DD network tab
2. Save `spans` as a file
3. Run: `./nesttrace.py [file name] [root_id]` to print the trace as a tree. You can replace `root_id` with any node id to focuse on a specific area
4. Run: `./tracedetails.py [file_name] [id]` to print all the details of a specific span

Example[s]:
`./nesttrace.py example.json 1`
`./tracedetails.py example.json 2`