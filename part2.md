
# Part 2 - Riak tasks
Solution was setup as follows:

- Version: Riak KV 2.2.3
- Set-up: Single node setup using memory backend to support secondary indexes
- BucketType Created and activated - hscicNews

##  Common Query Caching
-- Generated a key using MD5 hash from the search string
-- To distinguish between AND/OR results this parameter was appended to the search string, an alternative was to use separate buckets to store the results.
-- I have truncated the MD5 hashed key to the first 5 letters for the purpose of this exercise.

|   Query|  Type |  MD5 Hask Key (truncated 5 chars) |
| ------------ | ------------ | ------------ |
|Care Quality Commission  |  OR |  73a00 |
|September 2004 | OR  |  0e74b |
|general population generally   |  OR | 8a3f9  |
| Care Quality Commission admission  |  AND | 85504  |
| general population Alzheimer  | AND  |  c3aeb |



Following commands Inserts 5 Common cache queries keys (generated as described above):


curl  -XPOST http://127.0.0.1:8098/types/hscicNews/buckets/search_results/keys/73a00 -H 'Content-Type: text/plain'  -d '0,1,2,3,4,5,6'
curl  -XPOST http://127.0.0.1:8098/types/hscicNews/buckets/search_results/keys/0e74b -H 'Content-Type: text/plain'  -d '9'
curl  -XPOST http://127.0.0.1:8098/types/hscicNews/buckets/search_results/keys/8a3f9 -H 'Content-Type: text/plain'  -d '6,8'
curl  -XPOST http://127.0.0.1:8098/types/hscicNews/buckets/search_results/keys/85504 -H 'Content-Type: text/plain'  -d '1'
curl  -XPOST http://127.0.0.1:8098/types/hscicNews/buckets/search_results/keys/c3aeb -H 'Content-Type: text/plain'  -d '6'

**Get Query example:**

curl -i http://127.0.0.1:8098/types/hscicNews/buckets/search_results/keys/73a00 -H 'Content-Type: text/plain'

------------


##  Monthly indexes

The articles are stored using the **ref** as the key in a bucket called **articles**. A secondary index has been created by combining month/year to create month_year_bin to allow searching.



Bash script created to read each line from the file. Read the Year/Month/Day and Contents from each line and insert into Riak.

The articles are stored using JSON format this allows flexibility for future proofing and allows meta data to be stored against the article and retrieved.


**Example of insert for : Article 0**

curl -XPOST http://127.0.0.1:8098/types/hscicNews/buckets/articles/keys/0 \
-H 'year_month_bin:June2013' \
-H 'Content-Type: application/json' \
-d '{"article_ref": 0,"year": 2013,"month":"June","Day": 05 ,month-year":"June2013", "Contents": "The majority of carers say they are extremely..."}'




**-- Get Article Keys(s) for June 2013**

curl http://127.0.0.1:8098/types/hscicNews/buckets/articles/index/year_month_bin/June2013

Returns Article Keys 0,2,3,4

**--Get article example**

curl http://127.0.0.1:8098/types/hscicNews/buckets/articles/keys/0

## Considerations

### Large  Data Sets

-1.  For a large number of articles we can consider bucket types and buckets to store articles that are bucketed by YEAR/MONTH/DAY. These buckets come at a low cost and can improve performance.
-2.  Ensure sufficient settings for open files limits


### Fault tolerance \ Redundancy \ Availability
1.  Install additional nodes for  high scale applications. I would introduce a minimum of 5 nodes for larger sites, this is recommended minimum to provide adequate fault tolerance. Configure the n_val parameter so multiple nodes will replication data minimising data loss. Also ensure correct operation of each node post installation using Riaknostic.

2. To support fault tolerance and maximise throughput configure software/hardware load balancers pointing to each node.
Software: HA proxy supports  a S/W based load balancer.
Hardware Load Balancer: Cloud solutions such as AWS offers a load-balancing solution through Elastic Load Balancer.
These provide round robin requests to maximise throughput. Improved Fault tolerance as we have multiple nodes to serve traffic if we get node failure(s).

1.  To support availability, we can create multiple nodes which can be configured within a Docker containers or multiple instances installed on separate VMs.
- We can then utilise services such as Elastic container service (AWS) to monitor docker images and schedule creation of an additional docker images on node failure.
- Multiple EC2 instances across multiple availability zones or regions. Auto-scaling group can be configured to spin up new EC2 instances if one of the VMs fail to provide high availability.


### Data Consistency
- If we require consistent data reads we may need to consider the parameters (-r ,-w) which signal number of nodes required for  a successful read or write. This is changing quroum value.
- When writing data for conflict resolution (multiple writes) we can have two strategies here
 	- Last one wins
 	- use vector clocks to auto resolve conflicts or manually merge.

### Multiple User case support (searching, data persistence)
- Our example used in memory caching, we can configure multiple backends to support various user cases. e.g. dblevel data for other data types i.e reference data or configure other datasources.
- Set up Riak search features this will enable us to use more sophisticated search features and directly query documents across multiple backend sources.
