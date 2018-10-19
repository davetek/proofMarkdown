---
title: Inventory Search Web Service
subtitle: ISWS Legacy API
template: apis.swig
path: isws
autotoc: true
sortOrder: 2
---

<private>

INTERNAL NOTE: The **ISWS** is maintained by EpICS team. 
</private>

The **Inventory Search Web Service (ISWS)** is a legacy API that allows users to search for presale vehicle listings and obtain detailed information about these vehicles from various channels of inventory, such as OVE, Auction Presales and Simulcast. 

The **ISWS** provides methods to retrieve sales schedule information, retrieve valid values for search parameters, retrieve open listings, and retrieve closed listings to which the user has access.


### Release Notes

#### August 15, 2017
The following changes were made to ensure that this API shows listing information that is consistent with that shown in Manheim user applications such as manheim.com.

- Retrieve Listings
    - Added **auctionComments** to the response 
    - Added **remarks** to the response

- Retrieve Listings by User Name
    - Added **auctionComments** to the response 
    - Added **remarks** to the response

<!--htmlCollapse:start:oldReleaseNotes-->

#### February 5, 2016

- Retrieve Listings 
	- Added **titleState** to the response 
	- Added **pickupLocationState** to the response 
	- Added **pickupLocationZip** to the response

- Retrieve Listings by User Name 
	- Added **titleState** to the response 
	- Added **pickupLocationState** to the response 
	- Added **pickupLocationZip** to the response

#### August 23, 2016

- Retrieve Sales Schedule Information 
	- Added **saleDateTime** to the response

- Retrieve Listings
	- Fixed **EXTERIOR_COLOR** filter
	- Fixed **SELLER** filter 
	- Fixed **CERTIFIED_VEHICLES** filter 
	- Fixed **VEHICLE_TYPE** filter 
	- Fixed **SALE_DATE** filter 

- Retrieve Listings by User Name 
	- Fixed **EXTERIOR_COLOR** filter
	- Fixed **SELLER** filter 
	- Fixed **CERTIFIED_VEHICLES** filter 
	- Fixed **VEHICLE_TYPE** filter 
	- Fixed **SALE_DATE** filter 

<!--htmlCollapse:end-->


### API Access - Using an API Key

This legacy API is accessed with an **API key**; it does **not** require an access token. An API key is assigned by Manheim specifically for accessing the ISWS API. You must provide your API key in the URL with each API request.




<a name="retrieveSalesScheduleInfo"></a>


### Retrieve Sales Schedule

This method allows a user to retrieve information about upcoming sales, to include the sale date, auction location, and sale channel. 



#### Endpoint

```
POST https://api.manheim.com/isws-basic/sales?api_key=API_KEY
```

The "API_KEY" placeholder should be replaced by the user's unique API key, assigned by Manheim for access to the **ISWS** API. 



#### Request Parameters


<!--htmlCollapse:start:paramTable01-->

The parameters in the following tables are passed in the POST body, with the exception of api_key as noted.

| Parameter     | Notes |
|---------------|-------|
| api_key       | **REQUIRED:** Unique number to give a certain user access to the API; inserted into the request URL as demonstrated in the example above |
| pageSize      | Numeric value that defines the number of items a returned in a single response; if not specified, defaults to 1000  |
| pageNumber    | Numeric value that defines the beginning page of a response based on the **pageSize** |
| sort          | Used to sort sales; accepted values may be found in the table below | 
| sortDirection | May be used in conjunction with **sort**; accepted values are "forward" or "reverse"; if not specified, default is "forward" |

The **sort** query parameter may use one of the values in the following table. If two listings have the same value for one of the items in the Default Sort Sequence (such as 'saleDate'), the listing will attempt to sort by the next item in the sequence. 

| *sort* Value      | Default Sort Sequence |
|-------------------|-----------------------------|
| SALE_END_DATETIME | saleDate, inventorySortValues, auctionName, laneNumber |
| LOCATION_LANE_RUN | auctionName, inventorySortValues, saleDate, laneNumber | 

**NOTE** that **inventorySortValues** is not a field returned in the JSON response. 

<!--htmlCollapse:end-->



#### Example Request and Response


This example shows a cURL request for sales schedules that passes the api_key in the URL and three parameters in the body: pageSize, pageNumber, and sort. The response will contain a subset of open sales (determined by pageSize and pageNumber), sorted by sale end date.

<!--htmlCollapse:start:codeSample01-->


```
curl -X POST \
  'https://api.manheim.com/isws-basic/sales?api_key=ab768b723bz5nduw4hgm33yc' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'pageSize=5&pageNumber=1&sort=SALE_END_DATETIME'
```

In the cURL command, -X identifies the request method, followed by the URL with query parameters; -H flags a request header, and -d is the request body containing the body parameters. 



##### Response

The API call would return a JSON object similar to the example JSON code below.


```
{
    "sales": [
        {
            "saleDate": "20180725",
            "uniqueId": "SALE.OVE.26380.0.0-0.0",
            "vehicleCount": 20,
            "auctionId": "NADE",
            "auctionName": "Manheim New Jersey",
            "laneNumber": "0",
            "saleYear": "2018",
            "eventSaleName": "TD Trans Assist NJ Cars Sale 07/25/2018 - 07/31/2018",
            "consignor": "0",
            "saleDateTime": "2018-07-25 16:30:00.0",
            "channel": "OVE"
        },
        {
            "saleDate": "20180727",
            "uniqueId": "SALE.OVE.26115.0.0-0.0",
            "vehicleCount": 291,
            "auctionId": "AAA",
            "auctionName": "166 Auto Auction",
            "laneNumber": "0",
            "saleYear": "2018",
            "eventSaleName": "Carvana Weekly Trade-In Sale 07/27/2018 - 07/30/2018",
            "consignor": "0",
            "saleDateTime": "2018-07-27 09:00:00.0",
            "channel": "OVE"
        },
        {
            "saleDate": "20180727",
            "uniqueId": "SALE.OVE.26656.0.0-0.0",
            "vehicleCount": 44,
            "auctionId": "CANM",
            "auctionName": "Canada Home Office",
            "laneNumber": "0",
            "saleYear": "2018",
            "eventSaleName": "FCA Remarketing Canada Open Weekend Event Sale - 07/27/2018 - 07/30/2018",
            "consignor": "0",
            "saleDateTime": "2018-07-27 10:00:00.0",
            "channel": "OVE"
        },
        {
            "saleDate": "20180727",
            "uniqueId": "SALE.OVE.26089.0.0-0.0",
            "vehicleCount": 162,
            "auctionId": "AAA",
            "auctionName": "Manheim Albany",
            "laneNumber": "0",
            "saleYear": "2018",
            "eventSaleName": "Barco Weekend 4x4 Truck Sale 07/27/2018 - 07/30/2018",
            "consignor": "0",
            "saleDateTime": "2018-07-27 10:00:00.0",
            "channel": "OVE"
        },
        {
            "saleDate": "20180727",
            "uniqueId": "SALE.OVE.26423.0.0-0.0",
            "vehicleCount": 610,
            "auctionId": "AAA",
            "auctionName": "166 Auto Auction",
            "laneNumber": "0",
            "saleYear": "2018",
            "eventSaleName": "U-Haul Weekend Event Sale 07/27/2018 - 07/30/2018",
            "consignor": "0",
            "saleDateTime": "2018-07-27 12:00:00.0",
            "channel": "OVE"
        }
    ],
    "totalSales": 1124
}
```

<!--htmlCollapse:end-->


<a name="commonReturnCodes"></a>


#### Common Return Codes

The following table provides a list of status codes that may be returned by this method and other methods in the API. 

<!--htmlCollapse:start:paramTable02-->

|Response Code   | Description | Possible Next Actions |
|----------------|-----------------|-----------------------|
|200 OK     | Successful response       | No action necessary | 
|400 Bad Request | Required parameter is invalid or missing | Correct the data error mentioned in the response and resubmit |
|403 Forbidden  | The API key used in the request may be malformed or the user may not have access to make the API request | Modify request and resubmit  |
|404 Not Found    | Data specified in the request was not found | Modify request and resubmit |
|405 Method Not Allowed | The HTTP method used in the request may be malformed. | Correct the error mentioned in the response and resubmit |
|500 Server Error | Critical error prevented the requested data from being retrieved; response may include details about the error's cause. | Verify and modify the request if necessary and resubmit; if error persists, data may not be available |
|596 596 Service Not Found | Request URL or HTTP method may be malformed | Modify request and resubmit  |

<!--htmlCollapse:end-->







<a name="retrieveFilteredVehicleListings"></a>

### Retrieve Open Listings 

This method can be used to retrieve open vehicle listings. In addition, you can filter listings by submitting optional parameters, such as INVENTORY_SOURCE, LOCATION, and MAKE. You can also specify pagination and sort the results.  


#### Endpoint

```
POST https://api.manheim.com/isws-basic/listings?api_key=API_KEY
```

The "API_KEY" placeholder should be replaced by the user's unique API key. 



#### Request Parameters 

The parameters in the table below are optional and must be passed in the body of the JSON request, unless otherwise noted. Values for each parameter can be obtained as described in the section ["Retrieve Filter Values for Listings"](/#/apis/legacy/isws#retrieveFilterValuesForListings "ISWS API"). 

<!--htmlCollapse:start:paramTable03-->


| Parameter             | Notes |
|-----------------------|-------|
| api_key               | **REQUIRED** in the API call URL |
| pageSize              | Numeric value that defines the number of items a returned in a single response; if not specified, defaults to 1000  |
| pageNumber            | Numeric value that defines the beginning page of a response based on the **pageSize** |
| sort                  | Used to sort listings; accepted values may be found in the table below | 
| sortDirection         | May be used in conjunction with **sort**; accepted values are "forward" or "reverse"; if not specified, default is "forward" |
| CERTIFIED_VEHICLES    | Not a field to be returned to the user in the response |
| CONDITION_INFORMATION | Not a field to be returned to the user in the response |
| CONDITION_GRADE       | Correlates to **ecrGrade** in the response |
| DOOR                  | Correlates to **doorCount** in the "Retrieve Vehicle Listings" method response |
| DRIVE_TRAIN           | Correlates to **driveTrain** in the response |
| ECR                   | Vehicles with an ECR will have one or more URLs in the **eCRurl** and **mobileCRurl** fields in the response |
| ENGINE                | Correlates to **engine** in the "Retrieve Vehicle Listings" method response | 
| EXTERIOR_COLOR        | Correlates to **exteriorColor** in the response | 
| FUEL_TYPE             | Correlates to **fuelType** in the response |
| INTERIOR_COLOR        | Correlates to **interiorColor** in the response |
| INTERIOR_TYPE         | Correlates to **interiorType** in the response |
| INVENTORY_SOURCE      | Correlates to **channel** in the response |
| LOCATION              | **LOCATION** name is associated with an **auctionId** in the response |
| MAKE                  | Correlates to **make** in the response |
| MMR_PRICE_MIN         | Correlates to **mmrPrice** in the response which is not available to all API users (**REQUIRES** numerical input, such as "12350") |
| MMR_PRICE_MAX         | Correlates to **mmrPrice** in the response which is not available to all API users (**REQUIRES** numerical input, such as "12350") |
| MODEL                 | Correlates to **model** in the response |
| MILEAGE_MIN           | Correlates to **mileage** in the response (**REQUIRES** numerical input, such as "12350") |
| MILEAGE_MAX           | Correlates to **mileage** in the response (**REQUIRES** numerical input, such as "12350") |
| PHOTO                 | Vehicles with images will have one or more URLs within the entity **images** in the response |
| REGION                | Each **auctionId** is associated with a specific **REGION** but the **REGION** is not returned to the user in the response |
| SALE_DATE             | Correlates to **saleDate** in the response and does not include vehicles from OVE (**REQUIRES** format of MM/DD/YYYY)| 
| SALVAGE               | Vehicles with **titleStatus="Salvage"** in the response |
| SELLER                | Correlates to **sellerName** field that is associated with a certain **SELLER** | 
| SELLER_TYPE           | Each **sellerName** is associated with a **SELLER_TYPE** (not a field to be returned in the response to the user) |
| STATE_PROVINCE        | Correlates to **pickupLocationState** in the "Retrieve Vehicle Listings" method response |
| TOP_TYPE              | Correlates to **roof** in the response |
| TRANSMISSION          | Correlates to **transmission** in the response |
| VEHICLE_TYPE          | Correlates to **typeCode** in the response | 
| YEAR                  | Correlates to **year** in the "Retrieve Vehicle Listings" method response |

<!--htmlCollapse:end-->


The **sort** query parameter may use any "Parameter" in the table below. If no **sortDirection** is passed along with the **sort** query parameter in the body of the request, the returned listings will be in the "Default Order" listed below. Certain parameters will sort by multiple fields if two listings have the same value for a field as shown in "Fields Sorted" below.

<!--htmlCollapse:start:paramTable04-->

| Parameter                     | Default Order   | Fields Sorted |
| ------------------------------| ----------------| --------------|
| AC                            | forward         | hasAirConditioning |
| CHANNEL                       | forward         | channel |
| ENGINE_TYPE                   | forward         | engine |
| EXTERIOR_COLOR                | forward         | exteriorColor, year, make, model, mileage |
| GRADE                         | reverse         | conditionGradeNumDecimal, year, make, model, mileage |
| INTERIOR_COLOR                | forward         | interiorColor, year, make, model, mileage |
| LANE_RUN                      | forward         | laneNumber, runNumber | 
| LOCATION_LANE_RUN             | forward         | auctionLocationState, auctionName, laneNumber, runNumber  |
| MAKE                          | forward         | make, model, year, mileage | 
| MMR                           | reverse         | mmrPrice, year, make, model, mileage | 
| MODEL                         | forward         | extendedModel, make, year, mileage | 
| ODOMETER                      | forward         | mileage, year, make, model |
| PICKUP_LOCATION               | forward         | pickupLocationState, year, make, model, mileage |
| RUN                           | forward         | runNumber, year, make, model, mileage |
| SALE_END_DATE_TIME            | reverse         | saleStartDate, year, make, model, mileage | 
| SELLER                        | forward         | sellerName, year, make, model, mileage |
| TOP_TYPE                      | forward         | roof |
| TRANSMISSION                  | reverse         | transmission |
| UPDATE_TIMESTAMP              | reverse         | updateTimestamp |
| VIN                           | forward         | vin, year, make, model, mileage | 
| YEAR                          | reverse         | year, make, model, mileage |

<!--htmlCollapse:end-->
 
 <a name="openListingSearchExample-noParam"></a>


#### Example Request and Response for an Open Listings Search - Unfiltered


The following example shows a cURL request for open vehicle listings and a portion of the corresponding JSON response. These instructions describe a simple search with no filter parameters.


<!--htmlCollapse:start:codeSample02-->

```
curl -X POST \
  'https://api.manheim.com/isws-basic/listings?api_key=dcyzumfdu27nkfu2rwwkj8jf' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
```

In the cURL command, -X identifies the request method, followed by the URL with query parameters; and -H flags a request header. This request does not specify any parameters, so there is no -d POST body line. 

The response would be similar to this excerpt:

```
{
    "totalListings": 138898,
    "listings": [
        {
            "saleInformation": {
                "channel": "SIMULCAST",
                "saleDate": "08/15/2018",
                "uniqueId": "SALE.SIMULCAST.114513.82.1-1000.BMWN",
                "auctionId": "OAA",
                "laneNumber": "25",
                "runNumber": "269",
                "saleNumber": "33",
                "saleYear": "2018",
                "groupCode": "OPEN",
                "auctionLocation": "Manheim Atlanta",
                "vehicleSaleURL": "https://simulcast.manheim.com/simulcast/checkRequirementsAndStartBuyerAuction.do?vehicleGroupKey=a:OAA_s:114513_c:BMWN_l:25_v:82_q:1-1000",
                "auctionStartDate": "2018-08-15 14:00:00.000000"
            },
            "vehicleInformation": {
                "typeCode": "X",
                "year": 2019,
                "model": "4 Series",
                "engine": "4 Cyl. Gasoline Turbo",
                "auctionComments": "mso,mso,VEHICLE LOCATED @ 300 RAYMOND HILL RD  NEWNAN GA 30265",
                "sellerTypes": [
                    "Rental"
                ],
                "exteriorColor": "Black",
                "interiorColor": "Black",
                "titleStatus": "Received at Auction",
                "titleState": "MSO",
                "bodyStyle": "Sedan",
                "extendedModel": "430I GC 430I SPORT",
                "images": [
                    {
                        "largeUrl": "https://images.cdn.manheim.com/20180716150131-bff34291-52c2-4e9f-b9fe-c37f85629632.jpg",
                        "smallUrl": "https://images.cdn.manheim.com/20180716150131-bff34291-52c2-4e9f-b9fe-c37f85629632/small.jpg",
                        "description": "FRONTLEFT",
                        "sequence": 0
                    },
                    {
                        "largeUrl": "https://images.cdn.manheim.com/20180716150132-c7f96172-75ff-402b-ac79-2f323a3b3611.jpg",
                        "smallUrl": "https://images.cdn.manheim.com/20180716150132-c7f96172-75ff-402b-ac79-2f323a3b3611/small.jpg",
                        "description": "REARRIGHT",
                        "sequence": 1
                    },
                    {
                        "largeUrl": "https://images.cdn.manheim.com/20180718123019-e40e2d19-ea2f-415b-8db9-e07812711d05.jpg",
                        "smallUrl": "https://images.cdn.manheim.com/20180718123019-e40e2d19-ea2f-415b-8db9-e07812711d05/small.jpg",
                        "description": "INTERIORFRONT",
                        "sequence": 2
                    },
                    {
                        "largeUrl": "https://images.cdn.manheim.com/20180718123018-dd7eb31a-a221-4350-a1f8-5089399bc9a8.jpg",
                        "smallUrl": "https://images.cdn.manheim.com/20180718123018-dd7eb31a-a221-4350-a1f8-5089399bc9a8/small.jpg",
                        "description": "DASHBOARD",
                        "sequence": 3
                    },
                    {
                        "largeUrl": "https://images.cdn.manheim.com/20180718123018-2ffb70f7-8ba4-4854-b132-53c52c68ab31.jpg",
                        "smallUrl": "https://images.cdn.manheim.com/20180718123018-2ffb70f7-8ba4-4854-b132-53c52c68ab31/small.jpg",
                        "description": "ODOMETER",
                        "sequence": 4
                    },
                    {
                        "largeUrl": "https://images.cdn.manheim.com/20180718123018-edf9c2a1-8c6e-493b-bdd6-a2f5dd6063c3.jpg",
                        "smallUrl": "https://images.cdn.manheim.com/20180718123018-edf9c2a1-8c6e-493b-bdd6-a2f5dd6063c3/small.jpg",
                        "description": "MFGTAG",
                        "sequence": 5
                    },
                    {
                        "largeUrl": "https://images.cdn.manheim.com/20180718123019-702cae83-3907-45e4-929c-a55f028df4a7.jpg",
                        "smallUrl": "https://images.cdn.manheim.com/20180718123019-702cae83-3907-45e4-929c-a55f028df4a7/small.jpg",
                        "description": "CARGO",
                        "sequence": 6
                    },
                    {
                        "largeUrl": "https://images.cdn.manheim.com/20180720112103-77efc3ee-d137-4fc9-8686-2b267eb50e25.jpg",
                        "smallUrl": "https://images.cdn.manheim.com/20180720112103-77efc3ee-d137-4fc9-8686-2b267eb50e25/small.jpg",
                        "description": "DAMAGE",
                        "sequence": 7
                    }
                ],
                "mid": "201900666940083",
                "locationZip": "43123-9731",
                "transmission": "Automatic",
                "vin": "WBA4J1C59KBM12837",
                "pickupLocationZip": "30349",
                "adjMmr": 0,
                "pickupLocation": "Manheim Atlanta",
                "pickupLocationState": "GA",
                "certified": false,
                "updateTimestamp": 20180813205535,
                "make": "BMW",
                "mileage": 9875,
                "asIs": false,
                "salvage": false,
                "hasAirConditioning": true,
                "fuelType": "Gasoline",
                "interiorType": "Leather",
                "pickupRegion": "Southeast",
                "hasEcr": true,
                "odometerUnits": "mi",
                "crURL": "https://insightcr.manheim.com/cr-display?conditionOrderId=9830438&workOrderNumber=5688939&locationCode=AAA&vehicleUniqueId=SIMULCAST.OAA.13442269",
                "mobileCrUrl": "https://m.manheim.com/mobile/condition_report?vehicle_id=SIMULCAST.OAA.13442269",
                "vehicleOptions": [
                    "50 State Emissions",
                    "ABS Brakes",
                    "Air Conditioning",
                    "Auto Leveling Headlights",
                    "Automatic Headlights",
                    "Automatic Transmission",
                    "Back-Up Camera",
                    "Blind Spot Monitor",
                    "Bluetooth Connection",
                    "Brake Assist System",
                    "Bucket Seats",
                    "Child Safety Locks",
                    "Climate Control",
                    "Convienience Package",
                    "Cruise Control",
                    "Daytime Running Lights",
                    "Driver Air Bag",
                    "Driver Assistance Package",
                    "Dual Zone A/C",
                    "Electrochromic Rearview Mirror",
                    "Electronic Stability Control",
                    "Engine Immobilizer",
                    "Fog Lamps",
                    "Front Floor Mats",
                    "HD Radio",
                    "HSW - Heated Steering Wheel",
                    "Heated Mirrors",
                    "Heated Seats - Front",
                    "Heated Seats-Front(s)",
                    "Heated Steering Wheel",
                    "Intermittent Wipers",
                    "Keyless Entry",
                    "Keyless Start",
                    "Lane Departure System",
                    "Leather Seats",
                    "Leather Steering Wheel",
                    "MP3 Compatible Stereo",
                    "Mirror Memory",
                    "Navigation System",
                    "Owner's Manual",
                    "Pass-Through Rear Seat",
                    "Power Folding Mirrors",
                    "Power Liftgate",
                    "Power Locks",
                    "Power Mirrors",
                    "Power Seats",
                    "Power Seats - Dual",
                    "Power Steering",
                    "Power Tilt/Sliding Sunroof",
                    "Power Windows",
                    "Rain Sensing Wipers",
                    "Rain Sensor",
                    "Rear Defroster",
                    "Rear Floor Mats",
                    "Rear Head Air Bag",
                    "Rear Parking Aid",
                    "Remote Trunk Release",
                    "Run Flat Tires",
                    "ST - Steptronic Transmission",
                    "Satellite Radio",
                    "Seat Memory",
                    "Security System",
                    "Steering Wheel Audio Control",
                    "Telematics",
                    "Tilt Steering Wheel",
                    "Tire Pressure Monitor",
                    "Tire Pressure Monitor System",
                    "Traction Control",
                    "Trip Computer",
                    "Turbocharged",
                    "Turn Signal Mirrors",
                    "Universal Garage Door Opener",
                    "Warranty Books",
                    "Wheels - Alloy",
                    "Woodgrain Interior Package"
                ],
                "ecrGrade": "4 - Clean",
                "ecrURL": "https://insightcr.manheim.com/cr-display?conditionOrderId=9830438&workOrderNumber=5688939&locationCode=AAA&vehicleUniqueId=SIMULCAST.OAA.13442269",
                "airbags": [
                    "Dual",
                    "Side"
                ],
                "drivetrain": "2 Wheel Drive",
                "roof": "Sun Roof",
                "vinPrefix": "WBA4J1C5",
                "yearCharacter": "K",
                "vdpURL": "https://www.manheim.com/members/powersearch/vehicleDetails.do?vin=WBA4J1C59KBM12837&vehicleUniqueId=SIMULCAST.OAA.13442269#vdp&cid=AFF-ISWS-dcyzumfdu27nkfu2rwwkj8jf",
                "mobileVdpURL": "https://m.manheim.com/mobile/vehicles2/SIMULCAST.OAA.13442269?cid=AFF-ISWS-dcyzumfdu27nkfu2rwwkj8jf",
                "offsiteFlag": true,
                "conditionGradeNumDecimal": 4.3,
                "lotId": "SIMULCAST.OAA.13442269"
            },
            "sellerInformation": {
                "sellerName": "BMW NORTH AMERICA"
            }
        },
        {
            "saleInformation": {
                "channel": "SIMULCAST",
                "saleDate": "08/15/2018",
                "uniqueId": "SALE.SIMULCAST.114513.82.1-1000.BMWN",
                "auctionId": "OAA",
                "laneNumber": "25",
                ...
```

<!--htmlCollapse:end-->


<a name="openListingSearchExample-withParam"></a>


#### Example Request and Response for an Open Listings Search - Filtered


The following example shows a cURL request for open vehicle listings and the corresponding JSON response.

<!--htmlCollapse:start:codeSample03-->

```
curl -X POST \
  'https://api.manheim.com/isws-basic/listings?api_key=dcyzumfdu27nkfu2rwwkj8jf' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'pageSize=1&pageNumber=1&INVENTORY_SOURCE=57&LOCATION=165&SALE_DATE=08%2F9%2F2018'
```

In the cURL command, -X identifies the request method, followed by the URL with query parameters; -H flags a request header, and -d is the request body containing the body parameters. 

This request filters listings by INVENTORY_SOURCE, LOCATION, and SALE_DATE, then limits the size of each response (page) to one listing, and retrieves the first of all the listings in the results. 


```
{
    "listings": [
        {
            "saleInformation": {
                "saleDate": "08/09/2018",
                "uniqueId": "SALE.SIMULCAST.114017.56.0-0.FOR",
                "auctionId": "MAA",
                "laneNumber": "7",
                "runNumber": "260",
                "saleNumber": "48",
                "saleYear": "2018",
                "auctionStartDate": "2018-08-09 10:00:00.000000",
                "groupCode": "FOR",
                "auctionLocation": "Manheim Pennsylvania",
                "vehicleSaleURL": "https://simulcast.manheim.com/simulcast/checkRequirementsAndStartBuyerAuction.do?vehicleGroupKey=a:MAA_s:114017_c:FOR_l:7_v:56_q:ALL",
                "channel": "SIMULCAST"
            },
            "vehicleInformation": {
                "year": 2018,
                "model": "Escape",
                "engine": "4 Cyl. Gasoline Turbo",
                "sellerTypes": [
                    "Factory"
                ],
                "vin": "1FMCU9HD4JUA72645",
                "pickupLocationZip": "17545-9746",
                "adjMmr": 20600,
                "adjFlag": "5",
                "pickupLocation": "Manheim Pennsylvania",
                "pickupLocationState": "PA",
                "certified": false,
                "updateTimestamp": 20180803055856,
                "make": "Ford",
                "trim": "SEL",
                "mileage": 15008,
                "asIs": false,
                "salvage": false,
                "hasAirConditioning": true,
                "exteriorColor": "White",
                "interiorColor": "Gray",
                "titleStatus": "Received at Auction",
                "titleState": "PA",
                "bodyStyle": "MPV",
                "extendedModel": "ESCAPE 4X4 4C SEL",
                "images": [
                    {
                        "largeUrl": "https://images.cdn.manheim.com/20180709193348-6070a0da-f0dd-403b-9fd0-6310ddc505fd.jpg",
                        "smallUrl": "https://images.cdn.manheim.com/20180709193348-6070a0da-f0dd-403b-9fd0-6310ddc505fd/small.jpg",
                        "description": "FRONTLEFT",
                        "sequence": 0
                    },
                    {
                        "largeUrl": "https://images.cdn.manheim.com/20180709193420-f09a2ee5-8d0f-4d8b-83dd-9159324ae54d.jpg",
                        "smallUrl": "https://images.cdn.manheim.com/20180709193420-f09a2ee5-8d0f-4d8b-83dd-9159324ae54d/small.jpg",
                        "description": "REARRIGHT",
                        "sequence": 1
                    },
                    {
                        "largeUrl": "https://images.cdn.manheim.com/20180709193407-9cde4821-f5e4-4754-a779-0328eea727c7.jpg",
                        "smallUrl": "https://images.cdn.manheim.com/20180709193407-9cde4821-f5e4-4754-a779-0328eea727c7/small.jpg",
                        "description": "INTERIORFRONT",
                        "sequence": 2
                    },
                    {
                        "largeUrl": "https://images.cdn.manheim.com/20180709193402-52c201c0-9dfc-45b8-8bb0-aa7913623fc4.jpg",
                        "smallUrl": "https://images.cdn.manheim.com/20180709193402-52c201c0-9dfc-45b8-8bb0-aa7913623fc4/small.jpg",
                        "description": "DASHBOARD",
                        "sequence": 3
                    },
                    {
                        "largeUrl": "https://images.cdn.manheim.com/20180709193400-56556786-8292-4666-8285-233438d5caae.jpg",
                        "smallUrl": "https://images.cdn.manheim.com/20180709193400-56556786-8292-4666-8285-233438d5caae/small.jpg",
                        "description": "ODOMETER",
                        "sequence": 4
                    },
                    {
                        "largeUrl": "https://images.cdn.manheim.com/20180709193352-072e5d54-28a0-4895-8b29-633f0d0e3534.jpg",
                        "smallUrl": "https://images.cdn.manheim.com/20180709193352-072e5d54-28a0-4895-8b29-633f0d0e3534/small.jpg",
                        "description": "MFGTAG",
                        "sequence": 5
                    },
                    {
                        "largeUrl": "https://images.cdn.manheim.com/20180709193413-e0970cf9-51ca-477b-817e-737a242ce4fb.jpg",
                        "smallUrl": "https://images.cdn.manheim.com/20180709193413-e0970cf9-51ca-477b-817e-737a242ce4fb/small.jpg",
                        "description": "CARGO",
                        "sequence": 6
                    }
                ],
                "mid": "201801766060072",
                "locationZip": "17545-9746",
                "transmission": "Automatic",
                "fuelType": "Gasoline",
                "interiorType": "Leather",
                "pickupRegion": "Northeast",
                "hasEcr": true,
                "odometerUnits": "mi",
                "remarks": "*RENT REP;CD;LTHR;4X4",
                "crURL": "https://insightcr.manheim.com/cr-display?conditionOrderId=9719713&workOrderNumber=5783828&locationCode=MAA&vehicleUniqueId=SIMULCAST.MAA.19874607",
                "mobileCrUrl": "https://m.manheim.com/mobile/condition_report?vehicle_id=SIMULCAST.MAA.19874607",
                "vehicleOptions": [
                    "50 State Emissions",
                    "ABS Brakes",
                    "Air Conditioning",
                    "Automatic Headlights",
                    "Automatic Transmission",
                    "Back-Up Camera",
                    "Bluetooth Connection",
                    "Brake Assist System",
                    "Bucket Seats",
                    "Child Safety Locks",
                    "Climate Control",
                    "Cruise Control",
                    "Daytime Running Lights",
                    "Driver Air Bag",
                    "Dual Zone A/C",
                    "Electronic Stability Control",
                    "Engine Immobilizer",
                    "Fog Lamps",
                    "Front Floor Mats",
                    "Heated Mirrors",
                    "Heated Seats-Front(s)",
                    "Intermittent Wipers",
                    "Keyless Entry",
                    "Leather Seats",
                    "Leather Steering Wheel",
                    "MP3 Compatible Stereo",
                    "Maintenance Book",
                    "Owner's Manual",
                    "Pass-Through Rear Seat",
                    "Power Liftgate",
                    "Power Locks",
                    "Power Mirrors",
                    "Power Seats",
                    "Power Steering",
                    "Power Windows",
                    "Rear Defroster",
                    "Rear Head Air Bag",
                    "Rear Parking Aid",
                    "Rear Spoiler",
                    "Remote Engine Start",
                    "Remote Trunk Release",
                    "Satellite Radio",
                    "Security System",
                    "Steering Wheel Audio Control",
                    "Telematics",
                    "Tilt Steering Wheel",
                    "Tinted Windows",
                    "Tire Pressure Monitor System",
                    "Traction Control",
                    "Trip Computer",
                    "Turbocharged",
                    "US EPA Label",
                    "Warranty Books",
                    "Wheels - Alloy"
                ],
                "ecrGrade": "4 - Clean",
                "ecrURL": "https://insightcr.manheim.com/cr-display?conditionOrderId=9719713&workOrderNumber=5783828&locationCode=MAA&vehicleUniqueId=SIMULCAST.MAA.19874607",
                "airbags": [
                    "Dual",
                    "Side"
                ],
                "drivetrain": "4 Wheel Drive",
                "roof": "Hard Top Roof",
                "vinPrefix": "1FMCU9HD",
                "yearCharacter": "J",
                "vdpURL": "https://www.manheim.com/members/powersearch/vehicleDetails.do?vin=1FMCU9HD4JUA72645&vehicleUniqueId=SIMULCAST.MAA.19874607#vdp&cid=AFF-ISWS-dcyzumfdu27nkfu2rwwkj8jf",
                "mobileVdpURL": "https://m.manheim.com/mobile/vehicles2/SIMULCAST.MAA.19874607?cid=AFF-ISWS-dcyzumfdu27nkfu2rwwkj8jf",
                "offsiteFlag": false,
                "conditionGradeNumDecimal": 4.6,
                "lotId": "SIMULCAST.MAA.19874607",
                "typeCode": "T"
            },
            "sellerInformation": {
                "sellerName": "FORD MOTOR CREDIT COMPANY LLC"
            }
        }
    ],
    "totalListings": 700
}
```

<!--htmlCollapse:end-->


#### Common Return Codes

This method returns the standard codes described in ["Common Return Codes"](/#/apis/legacy/isws#commonReturnCodes "ISWS API") in the ["Retrieve Sales Schedule Information"](/#/apis/legacy/isws#retrieveSalesScheduleInfo "ISWS API") section.



<a name="retrieveFilterValuesForListings"></a>

### Retrieve Filter Values for Listings

You can use filters with listings requests to limit the response to the items you are interested in, such as in-lane listings at a single auction location, for example. This method returns an array of **name** and **id** values for any of the filter parameters. The **id** value is submitted in a listings request.


#### Endpoint

```
GET https://api.manheim.com/isws-basic/parameters/PARAMETER?api_key=API_KEY
```

The "PARAMETER" placeholder should be replaced with a valid search parameter, and "API_KEY" should be replaced by the user's unique API key. 



#### Request Parameters

<!--htmlCollapse:start:paramTable05-->


| Parameter             | Definition |
|-----------------------|------------|
| CERTIFIED_VEHICLES    | Certain makes of vehicles that have dealer certification (currently Audi and Volkswagen) |
| CONDITION_INFORMATION | Location of the information regarding the condition of the vehicle, such as “With the Seller” | 
| CONDITION_GRADE       | Value of the numerical form of the condition grade, such that “5.0” is equivalent to “5 - Extra Clean” | 
| DOOR                  | Number of doors of a vehicle |
| DRIVE_TRAIN           | Type of drive train a vehicle may have, such as “2 Wheel Drive” | 
| ECR                   | Vehicles with an Electronic Condition Report (ECR) to detail information about the state of the vehicle |  
| ENGINE                | Engine types for a vehicle |
| EXTERIOR_COLOR        | Colors for the exterior of a vehicle | 
| FUEL_TYPE             | Fuel types a vehicle may use |
| INTERIOR_COLOR        | Colors for the interior of a vehicle | 
| INTERIOR_TYPE         | Materials for the interior of a vehicle, such as “Vinyl” |  
| INVENTORY_SOURCE      | Sources of inventory for Manheim vehicles | 
| LOCATION              | Locations that may have vehicles | 
| MAKE                  | Make of the vehicle, used in the **makes** query parameter |
| MODEL                 | Models of a vehicle based on the **makes** query parameter | 
| PHOTO                 | Vehicles with photos |  
| REGION                | Area into which vehicle listings are partitioned in the United States such as “Southeast” or into another country, such as “Canada” | 
| SALVAGE               | Vehicles that are marked as “salvage”  |  
| SELLER                | Specific seller registered to a sellerName based on **sellerTypes** query parameter |
| SELLER_TYPE           | Types of sellers, such as “Bank” or “Dealer,” that may be used in the **sellerTypes** query parameter | 
| STATE_PROVINCE        | States and provinces for both United States and Canada listings |
| TOP_TYPE              | Describes the roof of the vehicle |  
| TRANSMISSION          | Transmission types for a vehicle |  
| VEHICLE_TYPE          | Type of vehicle, such as "Car"   |
| YEAR                  | Available years of vehicles | 

Some of the request parameters can only be obtained with the value of a related parameter, as described in the table below. 


#### Query String Parameters

| Parameter   | Notes |
|-------------|-------|
| api_key     | **Required** in the endpoint URL |
| makes       | **Required** in the endpoint URL when retrieving **MODEL** parameter values |
| sellerTypes | **Required** in the endpoint URL when retrieving **SELLER** parameter values |

To retrieve listings for a specific **MAKE** and **MODEL**, for example, first submit the **MAKE** parameter to retrieve all available manufacturers, and then use one of the MAKE id's in a request for the **MODEL**s for that make. See the 

<!--htmlCollapse:end-->



#### Example Request and Response 

##### Example: Obtaining INVENTORY_SOURCE Parameter Values

This example shows a request for INVENTORY_SOURCE parameter values, and the associated response. One of the inventory source id's could then be used to obtain listings for a particular inventory source such as Simulcast or Manheim Express. 


<!--htmlCollapse:start:codeSample04-->

Because the make ID is required to search for a model, the user would first use the /parameters/MAKE endpoint with their unique API key to retrieve all valid manufacturer names and the associated id's. 

```
GET https://api.manheim.com/isws-basic/parameters/INVENTORY_SOURCE?api_key=ab768b723bz5nduw4hgm33yc
```

Response excerpt:

```
{
    "parameterValues": [
        {
            "name": "OVE",
            "id": 53
        },
        {
            "name": "Simulcast",
            "id": 57
        },
        {
            "name": "In Lane",
            "id": 56
        },
        {
            "name": "Manheim Express",
            "id": 1359583
        },
        {
            "name": "BMW Group Direct",
            "id": 1358247
        },
        {
            "name": "Volvo Cars Direct Auction",
            "id": 1358248
        },
        {
            "name": "Nissan Infiniti Remarketing Private Store",
            "id": 1358372
        }
    ],
    "parameterType": "INVENTORY_SOURCE"
}
```

<!--htmlCollapse:end-->



##### Example: Obtaining MAKE and MODEL Parameter Values

In this example, the API is used to retrieve MODEL parameter values for a particular vehicle MAKE. 


<!--htmlCollapse:start:codeSample05-->

Because the make ID is required to search for a model, the user would first use the /parameters/MAKE endpoint with their unique API key to retrieve all valid manufacturer names and the associated id's. 

```
GET https://api.manheim.com/isws-basic/parameters/MAKE?api_key=ab768b723bz5nduw4hgm33yc
```

Response excerpt:

```
{
    "parameterValues": [
        {
            "name": "4-STAR",
            "id": 101000456
        },
        {
            "name": "4-Star Trailers",
            "id": 101001529
        },
        ...,
        {
            "name": "Audi",
            "id": 101000005
        },
        ...
```

The user could then retrieve models for the Audi make by using the MODEL parameter, their unique API key, and the "makes" parameter set to the id for Audi as shown: 


```
GET https://api.manheim.com/isws-basic/parameters/MODEL?api_key=ab768b723bz5nduw4hgm33yc&makes=101000005
```

The response would include all Audi models as shown in this truncated example:


```
{
    "parameterValues": [
        {
            "name": "100",
            "id": 102000023
        },
        {
            "name": "100 Series",
            "id": 102185402
        },
        {
            "name": "200",
            "id": 102001804
        },
        {
            "name": "200 Series",
            "id": 102185403
        },
        {
            "name": "4000",
            "id": 102001201
        },
        {
            "name": "4000/GT Coupe",
            "id": 102184318
        },
        {
            "name": "4000CS",
            "id": 102184319
        },
        ...
    ],
    "parameterType": "MODEL"
}

```

<!--htmlCollapse:end-->


#### Common Return Codes

This method returns the standard codes described in ["Common Return Codes"](/#/apis/legacy/isws#commonReturnCodes "ISWS API") in the ["Retrieve Sales Schedule Information"](/#/apis/legacy/isws#retrieveSalesScheduleInfo "ISWS API") section.







### Retrieve Listings by User Name

This method retrieves all listings to which the user has access, including any closed sale listings the user may have access to. This method also allows a user to retrieve additional fields in the response that they may have access to. 

Vehicle listings include notes entered in multiple Manheim applications. If present, these notes will be returned in the "comments", "announcements", "auctionComments", and/or "remarks" fields. 



#### Endpoint

```
POST https://api.manheim.com/isws-basic/listingsByUserName?api_key=API_KEY
```

The "API_KEY" placeholder should be replaced by the user's unique API key. 



#### Request Parameters

This method accepts the same request parameters as the ["Retrieve Vehicle Listings"](/#/apis/legacy/isws#retrieveVehicleListings "ISWS API") method. **To retrieve listings by user name, you must also include an "authorized-user-name" header**, as described in the following table: 

| Header Parameter      | Notes |
|-----------------------|-------|
| authorized-user-name  | Online User Name provided by Manheim for accessing Manheim websites, such as Manheim.com and OVE.com; allows a user to view closed sale listings; **REQUIRED** in the header of the API call |




#### Example Request and Response 

This example shows a cURL request for all listings that the user has access to and the corresponding JSON response.

<!--htmlCollapse:start:codeSample06-->

```
curl -X POST \
  'https://api.manheim.com/isws-basic/listingsByUserName?api_key=ab768b723bz5nduw4hgm33yc' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'authorized-user-name: janedoe' \
```

In the cURL command, -X identifies the request method, followed by the URL with query parameters; -H flags a request header, and -d is the request body containing the body parameters. 

**NOTE** that **sellerInformation** fields may not be available to all users. If a user does not have access to a field, the response will omit those fields. 

**NOTE** All **URLs** that are present in the example response contain the parameter **auth_tkt,** which is a unique number associated with the user. The **URLs** also contain the username, first name, and last name of the API user.

The API would return a JSON object similar to the example JSON code below. 

```
{
  "listings": [
    {
      "saleInformation": {
        "auctionId": "ISAA",
        "saleDate": "07/07/2016",
        "dealerGroup": "FOR",
        "saleYear": "2016",
        "auctionStartDate": "2016-07-07 04:45:00.000000",
        "auctionEndDate": "2016-07-11 03:45:00.000000",
        "auctionLocation": "RIO LINDA",
        "vehicleSaleURL": "https://www.manheim.com/secureredirect?product=OVE&url=/vdp/vin/5LMCJ1A99FUJ00895&auth_tkt=xxxxxxxxxxxxxusername%21%21firstName%2BlastName",
        "channel": "OVE"
      },
      "vehicleInformation": {
        "vin": "5LMCJ1A99FUJ00895",
        "make": "Lincoln",
        "images": [
          {
            "largeUrl": "https://images.cdn.manheim.com/20160706222902-c2baf0c0-bf8f-423c-8c57-9487a5f7466a.jpg?auth_tkt=xxxxxxxxxxxxxusername%21%21firstName%2BlastName",
            "smallUrl": "https://images.cdn.manheim.com/20160706222902-c2baf0c0-bf8f-423c-8c57-9487a5f7466a.jpg?auth_tkt=xxxxxxxxxxxxxusername%21%21firstName%2BlastName",
            "description": "Image 1",
            "sequence": 1
          },
          {
            "largeUrl": "https://images.cdn.manheim.com/20160706222904-02a673a3-36c0-46cb-a44b-2613580f0685.jpg?auth_tkt=xxxxxxxxxxxxxusername%21%21firstName%2BlastName",
            "smallUrl": "https://images.cdn.manheim.com/20160706222904-02a673a3-36c0-46cb-a44b-2613580f0685.jpg?auth_tkt=xxxxxxxxxxxxxusername%21%21firstName%2BlastName",
            "description": "Image 2",
            "sequence": 2
          },
          {
            "largeUrl": "https://images.cdn.manheim.com/20160706222905-471661a3-de20-4eed-b956-9e1f927a0431.jpg?auth_tkt=xxxxxxxxxxxxxusername%21%21firstName%2BlastName",
            "smallUrl": "https://images.cdn.manheim.com/20160706222905-471661a3-de20-4eed-b956-9e1f927a0431.jpg?auth_tkt=xxxxxxxxxxxxxusername%21%21firstName%2BlastName",
            "description": "Image 3",
            "sequence": 3
          }
        ],
        "pickupLocationZip": "95673",
        "mmrPrice": "24300",
        "pickupLocation": "RIO LINDA",
        "pickupLocationState": "CA",
        "asIs": false,
        "salvage": false,
        "mileage": 32320,
        "updateTimestamp": 20160708000000,
        "mid": "201503269353665",
        "frameDamage": "0",
        "priorPaint": "0",
        "buyerGroupId": "21",
        "exteriorColor": "Brown",
        "titleStatus": "Not Specified",
        "titleState": "CA",
        "extendedModel": "MKC",
        "locationZip": "95673",
        "comments": "ECOBOOST,MLT, Front Wheel Drive, Automatic Transmission, 4 Cylinder Gas, 50 State Emissions",
        "transmission": "Automatic",
        "hasAirConditioning": false,
        "crURL": "http://www.edgepipeline.com/CarReport.aspx?A=BSAA&AVID=22643.17700&drill=ext&auth_tkt=xxxxxxxxxxxxxusername%21%21firstName%2BlastName",
        "mobileCrUrl": "http://www.edgepipeline.com/CarReport.aspx?A=BSAA&AVID=22643.17700&drill=ext",
        "buyNowPrice": "19800",
        "ecrGrade": "3 - Average",
        "ecrURL": "http://www.edgepipeline.com/CarReport.aspx?A=BSAA&AVID=22643.17700&drill=ext&auth_tkt=xxxxxxxxxxxxxusername%21%21firstName%2BlastName",
        "vinPrefix": "5LMCJ1A9",
        "yearCharacter": "F",
        "vdpURL": "https://www.manheim.com/secureredirect?product=OVE&url=/vdp/vin/5LMCJ1A99FUJ00895&auth_tkt=xxxxxxxxxxxxxusername%21%21firstName%2BlastName",
        "mobileVdpURL": "https://m.manheim.com/mobile/vehicles2/OVE.ISAA.79740348?auth_tkt=xxxxxxxxxxxxxusername%21%21firstName%2BlastName",
        "offsiteFlag": false,
        "conditionGradeNumDecimal": 3.7,
        "lotId": "OVE.ISAA.79740348",
        "year": 2015,
        "typeCode": "SUV"
      },
      "sellerInformation": {
        "city": "xxxx",
        "postalCode": "xxxx",
        "sellerName": "Ford",
        "auctionAccessRepNumber": "xxxxx",
        "contact": "xxx-xxx-xxxx",
        "addressOne": "xxx",
        "addressTwo": "xxxx",
        "phoneNumber": "xxx-xxx-xxxx",
        "state": "xxx"
      }
    }, 
  "totalListings": 1
}
```

<!--htmlCollapse:end-->


#### Common Return Codes

This method returns the standard codes described in ["Common Return Codes"](/#/apis/legacy/isws#commonReturnCodes "ISWS API") in the ["Retrieve Sales Schedule Information"](/#/apis/legacy/isws#retrieveSalesScheduleInfo "ISWS API") section.



