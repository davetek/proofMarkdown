---
title: /valuations
subtitle: Valuations
template: apis.swig
path: valuations
autotoc: true
sortOrder: 1
---



<private>



INTERNAL NOTE: The **Valuations** API was developed and is maintained by EpICS Team. 


</private>



There are two versions of the **Valuations** API, **Version 1** and **Version 2**. Version 2 is the latest version. You can choose which version to use by adding a header in the API call. If you specify version 1 in the request header, you will get an older API version. If you specify version 2 or do not request a specific version, you will get the latest version. 

Information on adding a header to an API call may be found in our [API Versioning](http://developer.manheim.com/#/versioning) guide. Information on the additions for the newest version may be found in the Release Notes section. 


 


### Release Notes 

#### October 2018
- Provided "include" request parameter to allow the requester to obtain retail, historical, and forecast data, in the methods ["Retrieve Batch Valuations by MID"](/#/apis/marketplace/valuations#retrieveBatchValuationsByMID "Retrieve Batch Valuations by MID") and ["Retrieve Batch Valuations by VIN"](/#/apis/marketplace/valuations#retrieveBatchValuationsByVIN "Retrieve Batch Valuations by VIN").


<!--htmlCollapse:start:oldReleaseNotes-->


<private>

#### September 2017
- Added a "samples" response field containing an MMRTransactionsWebService href, to allow the requester to access MMR Price and Transactions data. This field was added to the methods ["Retrieve Valuations by VIN"](/#/apis/marketplace/valuations#retrieveValuationsByVIN "Retrieve Valuations by VIN"), ["Retrieve Valuations by MID"](/#/apis/marketplace/valuations#retrieveValuationsByMID "Retrieve Valuations by MID"), ["Search Valuations"](/#/apis/marketplace/valuations#searchValuations "Search Valuations"), ["Retrieve Batch Valuations by MID"](/#/apis/marketplace/valuations#retrieveBatchValuationsByMID "Retrieve Batch Valuations by MID"), and ["Retrieve Batch Valuations by VIN"](/#/apis/marketplace/valuations#retrieveBatchValuationsByVIN "Retrieve Batch Valuations by VIN").  


</private>


#### August 2017
- Provided new optional request parameter "orgId" to allow the API to capture the requester of the valuation, even when the request is made through another company or via a link to a Manheim web application. This applies to the methods ["Retrieve Valuations by VIN"](/#/apis/marketplace/valuations#retrieveValuationsByVIN "Retrieve Valuations by VIN"), ["Retrieve Valuations by MID"](/#/apis/marketplace/valuations#retrieveValuationsByMID "Retrieve Valuations by MID"), ["Search Valuations"](/#/apis/marketplace/valuations#searchValuations "Search Valuations"), ["Retrieve Valuations by MID"](/#/apis/marketplace/valuations#retrieveValuationsByMID "Retrieve Valuations by MID"), and ["Retrieve Batch Valuations by VIN"](/#/apis/marketplace/valuations#retrieveBatchValuationsByVIN "Retrieve Batch Valuations by VIN").
- Provided new optional request parameters "zipCode", "geoLocation" to identify the location of the vehicle. This applies to the methods ["Retrieve Valuations by VIN"](/#/apis/marketplace/valuations#retrieveValuationsByVIN "Retrieve Valuations by VIN"), ["Retrieve Valuations by MID"](/#/apis/marketplace/valuations#retrieveValuationsByMID "Retrieve Valuations by MID"), ["Search Valuations"](/#/apis/marketplace/valuations#searchValuations "Search Valuations"), ["Retrieve Batch Valuations by MID"](/#/apis/marketplace/valuations#retrieveBatchValuationsByMID "Retrieve Batch Valuations by MID"), and ["Retrieve Batch Valuations by VIN"](/#/apis/marketplace/valuations#retrieveBatchValuationsByVIN "Retrieve Batch Valuations by VIN").



#### May 2017
- For ["Retrieve Valuations by VIN"](/#/apis/marketplace/valuations#retrieveValuationsByVIN "Retrieve Valuations by VIN") method, added "bestMatch" field to response described in item table in "Response Parameters" section and in second example in "Example JSON Response" section


#### May 2017

- Provided more matches to searches or requests by VIN by including valuations that do not have pricing information. This also reduces the likelihood of 404 errors that previously occurred when no pricing information existed for a specific vehicle
- Updated response message for "404 Not Found" in the "Common Return Codes" table, in three sections: ["Retrieve Valuations by VIN"](/#/apis/marketplace/valuations#retrieveValuationsByVIN "Retrieve Valuations by VIN"), ["Retrieve Valuations by MID"](/#/apis/marketplace/valuations#retrieveValuationsByMID "Retrieve Valuations by MID"), and ["Search Valuations"](/#/apis/marketplace/valuations#searchValuations "Search Valuations")


#### January 2017 

- Added individual adjustment fields for color, grade and odometer for ["Retrieve Valuations by MID"](/#/apis/marketplace/valuations#retrieveValuationsByMID "Retrieve Valuations by MID") method 
- Added an "href" field for the [Samples API](/#/apis/marketplace/samples "Samples API") for the methods ["Retrieve Valuations by MID"](/#/apis/marketplace/valuations#retrieveValuationsByMID "Retrieve Valuations by MID"), ["Retrieve Valuations by VIN"](/#/apis/marketplace/valuations#retrieveValuationsByVIN "Retrieve Valuations by VIN") and "Retrieve Valuations by Search" 
- Updated formatting of this page to group information by method



#### December 2016 

- Added **NEW** ["Retrieve Batch Valuations by MID"](/#/apis/marketplace/valuations#retrieveBatchValuationsByMID "Retrieve Batch Valuations by MID") method
- Added **NEW** ["Retrieve Batch Valuations by VIN"](/#/apis/marketplace/valuations#retrieveBatchValuationsByVIN "Retrieve Batch Valuations by VIN") method 
- Added **NEW** "Retrieve a Single Region" method
- Added "Region" field to the **Valuations** response when the "region" query parameter is invoked 
- Updated "Retrieve Region by Auction" endpoint
- Updated response to "Retrieve All Regions" to include endpoints for each region 
- Updated JSON Attributes for the method "Retrieve All Regions"
- Updated JSON Attributes for the method "Retrieve a Single Region"
- Added JSON Attributes for the method "Retrieve Region by Auction"
- Added JSON Attributes for ["Retrieve Batch Valuations by MID"](/#/apis/marketplace/valuations#retrieveBatchValuationsByMID "Retrieve Batch Valuations by MID")
- Added JSON Attributes for ["Retrieve Batch Valuations by VIN"](/#/apis/marketplace/valuations#retrieveBatchValuationsByVIN "Retrieve Batch Valuations by VIN")

<!--htmlCollapse:end-->



### Overview 

The **Valuations** API allows consumers to retrieve valuations, which are indicators of wholesale prices drawn from the [Manheim Market Report](https://www.manheim.com/services/valuation?WT.svl=m_hdr_mnav_buy_valuation "Manheim - Valuation"). The pricing calculations are based on more than 10 million sales transactions for the previous 13 months, and pricing data is refreshed nightly. This REST API is a replacement of our previous SOAP versions as discussed below in our overview of switching from our SOAP to REST APIs. 

API users may request valuations by ID, by VIN or by year, make, model and trim.  Users may retrieve information about the current edition of the **Manheim Market Report** and information about the geographic regions into which the information is partitioned. Information about each region or auction is available through the **Valuations** API. Users may retrieve valuations individually or by a batch call.

Clients may reach out to us for access to a testing environment. 






<a name="retrieveValuationsByVIN"></a>


### Retrieve Valuations by VIN

#### Endpoints

```
GET https://integration1.api.manheim.com/valuations/vin/VIN

GET https://integration1.api.manheim.com/valuations/vin/VIN/SUBSERIES

GET https://integration1.api.manheim.com/valuations/vin/VIN/SUBSERIES/TRANSMISSION

```

"VIN" in the URL should be replaced by the VIN of the vehicle. "SUBSERIES" and "TRANSMISSION" should be replaced by the subseries identifier (e.g. "528I MAN") and transmission identifier (e.g. "M").


#### Description 

This method allows a user to use the VIN of a vehicle to retrieve valuations. Manheim returns any vehicle styles that match the VIN provided, even if they are not an exact match.

**NOTE**: You can see how response parameters from this API match the fields in the [Manheim Market Report](https://www.manheim.com/services/valuation?WT.svl=m_hdr_mnav_buy_valuation "Manheim - Valuation") by referring to ["How API Response Parameters Map to the Manheim Market Report"](/#/apis/marketplace/valuations#responseMapToMMR  "Response Parameters Map to MMR UI").





#### Common Return Codes 


|Response Code | Response Message | Possible Next Actions | 
|--------------|------------------|------------------------|
|200 OK   | Body contains the requested information | Successful response; no actions necessary |
|400 Bad Request | **ERROR:** Invalid VIN | VIN may contain invalid characters or may be the wrong length; check and resubmit |
|401 Unauthorized |**ERROR:** Developer inactive | API token may be malformed or the user does not have access; check the token or contact Manheim for further support |
|404 Not Found | **ERROR:** Matching vehicles not found | URL may be malformed or the requested valuation does not exist; check and resubmit |
|500 Server Error | **ERROR:** Unknown Error | Resubmit the request; if issue still exists contact Manheim for support |
|596 596 | **ERROR:** 596 Service Not Found | URL may be malformed; check the method name and resubmit |


 

#### Request Parameters 

This method requires only the VIN in the URL. The user may also enter a vehicle's subseries or its transmission into the URL. 

|Parameter |Type | Requirement | Description |
|----------|-----|-------------|--------------|
|VIN          |String |REQUIRED | vehicle identification number (VIN) of a vehicle |
|SUBSERIES    |String | REQUIRED if "TRANSMISSION" is present | Further division  of a vehicle, such as "SE" or "LE" | 
|TRANSMISSION|String|OPTIONAL | Details the transmission of a vehicle, with "A" for "Automatic" and "M" for "Manual" (only available for certain vehicles) |
 

<a name="queryParameters"></a>


The URL may also include an OPTIONAL query string that includes one or more of the parameters in the following table. 

| Parameter | Type | Description |
|-----------|-------|------------|
| country   | String| API calls will default to US if this parameter is omitted; accepted values: US for United States, CA for CANADA |
| odometer  |Integer| Accepts numeric values but currently matches only exact values rather than a range of values |
| region    |String |API calls will default to NA if this parameter is omitted. For vehicles in the US, use one of the following region codes: SE, NE, MW, SW or WC. For Canada, use ON, QU, AT or WE. See ["Retrieve All Regions"](/#/apis/marketplace/valuations#retrieveAllRegions "Valuations API") for more information.|
| include   |String | Accepts any comma-separated combination of the following, in any order: retail, forecast, historical |
| color     |String | External color of the vehicle; accepted values may be retrieved from the request "Retrieve All Colors" |
| grade     |Integer| Condition of the vehicle such that "30" is equivalent to "3.0" | 
| orgId     |String | Characters that identify the individual or organization requesting the valuation. Coordinate with your Manheim account representative to set up orgId's. |
| zipCode   |String | Location of the vehicle as a 5-digit postal code, e.g. "30019" |
| geoLocation  |String | Location of the vehicle in the form of a latitude and longitude |



#### Example JSON Requests

##### Request for a specific VIN 

The following example shows a request for a specific VIN.

```
GET https://integration1.api.manheim.com/valuations/vin/WBA3C1C5XFP85
```

If the value would otherwise contain whitespace, the whitespace character should be omitted or replaced with "%20". 

If the value contains a "/", it may be replaced with "%2F". 


##### Request with subseries & transmission

The user may make a more specific request by specifying the subseries and transmission of the vehicle after the VIN. The following example shows a request for a specific VIN (WBA3C1C5XFP853102), subseries (328i), and transmission (A).

```
GET https://integration1.api.manheim.com/valuations/vin/WBA3C1C5XFP853102/328i/A
```
 
##### Request with odometer, region, include

The URL may also contain a query string similar to the following, to obtain a valuation adjusted for **odometer** and **region**, and including retail values. 

```
GET https://integration1.api.manheim.com/valuations/vin/JM1BL1L81D?odometer=10000&region=se&include=retail
```

##### Request with color & grade

The query may also include parameters for **color** and **grade** as shown in the following example. 

```
GET `https://integration1.api.manheim.com/valuations/vin/WBA3C1C5XFP853102?color=WHITE&grade=31&odometer=20000&region=NE`
```

##### Request with ZIP code

The query may also include a **ZIP code**, as shown in the following example. This does not affect the immediate response, but may help Manheim define regional adjustments more accurately in the future.

```
GET `https://integration1.api.manheim.com/valuations/vin/WBA3C1C5XFP853102?color=WHITE&grade=31&odometer=20000&region=NE&zipCode=74051`
```

##### Request with geolocation

The query may also include a **geolocation**, as shown in the following example. This does not affect the immediate response, but may help Manheim define regional adjustments more accurately in the future.

```
GET `https://integration1.api.manheim.com/valuations/vin/WBA3C1C5XFP853102?color=WHITE&grade=31&odometer=20000&region=NE&&geoLocation==33.9335,-84.3958`
```

##### Request with orgId

To identify the requestor **organization / individual**, pass the *orgId* parameter as shown in this query example: 

```
GET https://integration1.api.manheim.com/valuations/id/201700625412724?country=US&odometer=10000&color=RED&grade=30&orgId=jDoe&zipCode=30328&geolocation=33.9335, -84.3958&include=retail,historical,forecast
```





<a name="responseFields"></a>



#### Response Parameters 



|Field    | Type   | Description | 
|---------|--------|--------------|
|href    | String | URL of the request |
|count    |Integer | Number of valuations returned |
|**items**| Array | Array containing an object for each valuation; fields in each valuation object are shown in the tables below |



Each item valuation is described by the fields in the table below. **Note** Some fields are only returned if specific parameters are included in the request.

|Field     | Type | Description | 
|-------------|---------|--------------|
| href       |String | URL of the valuation containing the Manheim ID (MID) of a unique vehicle valuation | 
| description | Object | Information about the vehicle |
| description.year |Integer| Year of the valuation vehicle |
| description.make |String |Make of the valuation vehicle |
| description.model |String |Model of the valuation vehicle |
| description.trim |String |Trim of the valuation vehicle |
| description.subSeries |String |Subseries of the valuation vehicle |
| description.transmission | String | Transmission of the valuation vehicle; may not always be returned |
| adjustedPricing | Object | Information about the valuation pricing adjusted by various factors |
| adjustedPricing.wholesale |Object| Information about the adjusted valuation of the vehicle at the auction |
| adjustedPricing.wholesale.above   |Integer| One standard deviation above the adjusted average valuation| 
| adjustedPricing.wholesale.average |Integer| Adjusted average valuation |
| adjustedPricing.wholesale.below   |Integer| One standard deviation below the adjusted average valuation|
| adjustedPricing.retail |Object| Information about the adjusted valuation of the vehicle in the consumer market |
| adjustedPricing.retail.above   |Integer| One standard deviation above the adjusted average MMR retail valuation | 
| adjustedPricing.retail.average |Integer |Adjusted average MMR retail value |
| adjustedPricing.retail.below   |Integer| One standard deviation below the adjusted average MMR retail valuation | 
| adjustedPricing.adjustedBy | Object | Information about the specific valuation adjustments when optional query parameters are invoked |
| adjustedPricing.adjustedBy.Color | String | Exterior color of the vehicle. Included if the color parameter was passed in the query, identifies the color, ex: "SILVER" |
| adjustedPricing.adjustedBy.Grade | String | If a grade parameter was passed in the query, identifies the grade, ex: "44" |
| adjustedPricing.adjustedBy.Odometer | String | If an odometer parameter was passed in the query, identifies the odometer value, ex: "30100" |
| adjustedPricing.adjustedBy.Region | String | If a region parameter was passed in the query, identifies the region set for the valuation; defaults to "NA" for "National" |
| wholesale    |Object| Information about the valuation of the vehicle at the auction |
| wholesale.above   |Integer| One standard deviation above the average| 
| wholesale.average |Integer| Average valuation |
| wholesale.below   |Integer| One standard deviation below the average |
| retail    |Object| Information about the expected value of the vehicle in the consumer market |
| retail.above   |Integer |One standard deviation above the average |
| retail.average |Integer |Average MMR retail value |
| retail.below   |Integer |One standard deviation below the average  |
| historicalAverages |Object | Information about average odometer readings and price values for past periods |
| historicalAverages.last30days | Object | MMR information from the past 30 days, regardless of the month |
| historicalAverages.last30days.odometer|Integer|Average odometer of the vehicles used to calculate the MMR during this time period | 
| historicalAverages.last30days.price   |Integer|Average price of the MMR for a specific vehicle during this time period |
| historicalAverages.lastMonth | Object |MMR information from the past month |
| historicalAverages.lastMonth.odometer|Integer|Average odometer of the vehicles used to calculate the MMR during this time period | 
| historicalAverages.lastMonth.price   |Integer|Average price of the MMR for a specific vehicle during this time period |
| historicalAverages.lastTwoMonths | Object |MMR information from the past two months |
| historicalAverages.lastTwoMonths.odometer|Integer|Average odometer of the vehicles used to calculate the MMR during this time period | 
| historicalAverages.lastTwoMonths.price   |Integer|Average price of the MMR for a specific vehicle during this time period |
| historicalAverages.lastSixMonths | Object |MMR information from the past six months |
| historicalAverages.lastSixMonths.odometer|Integer|Average odometer of the vehicles used to calculate the MMR during this time period | 
| historicalAverages.lastSixMonths.price   |Integer|Average price of the MMR for a specific vehicle during this time period |
| historicalAverages.lastYear | Object |MMR information from the past year | 
| historicalAverages.lastYear.odometer|Integer|Average odometer of the vehicles used to calculate the MMR during this time period | 
| historicalAverages.lastYear.price   |Integer|Average price of the MMR for a specific vehicle during this time period |
| forecast       | Object | Information about the predicted MMR for the vehicle|
| forecast.nextMonth  | Object | MMR information for the upcoming month |
| forecast.nextMonth.wholesale |Integer |Predicted MMR price of a vehicle for auction sale |
| forecast.nextMonth.retail    |Integer|Predicted MMR price of a vehicle for consumer sale |
| forecast.nextYearv   | Object| MMR information for the upcoming year |
| forecast.nextYear.wholesale |Integer |Predicted MMR price of a vehicle for auction sale |
| forecast.nextYear.retail    |Integer |Predicted MMR price of a vehicle for consumer sale |
| averageOdometer |Integer| Average number for the odometer on the vehicles used in the valuation |
| odometerUnits   |String | Unit of measurement for the odometer |
| averageGrade    |Integer| Average vehicle grade of the valuation, such that "50" is equivalent to "5.0" | 
| currency        |String | Type of currency used, such as "USD" for "U.S. Dollars" |
| bestMatch       |Boolean| If present, indicates that this item is the best MMR match found for the VIN provided |  







<private> 


Internal Only: The "**samples**" and "**samples.href**" fields are provided in the API response.

|Field          | Type | Description |
|---------------|------|-------------|
| samples       |Object| Contains a reference to the MMRTransactionsWebService for retrieving price and transactions data |  
| samples.href  |String| URL for MMRTransactionsWebService data for the applicable vehicle  |



Internal Only: If the "**odometer**" query parameter is used, the "**adjustedBy**" field will contain additional information with one or more of the fields below.  

|Field  | Type | Description |
|-------|-------|--------|
| OdometerAdjustmentValue|Integer|Amount the valuation was adjusted based on the odometer |


Internal Only: If the "**region**" query parameter is used, the **"adjustedBy" field** will contain additional information with one or more of the fields below.  

|Field  | Type | Description |
|-------|-------|--------|
| RegionAdjustmentValue | Object | Information about the amount for which the valuation was adjusted by region |
| RegionAdjustmentValue.wholesale | Object | Information about the wholesale valuation pricing |
| RegionAdjustmentValue.wholesale.average |Integer| Average adjusted valuation |
| RegionAdjustmentValue.retail | Object | Information about the adjusted retail valuation pricing based on the region when using the "retail" query parameter |
| RegionAdjustmentValue.retail.average |Integer |Average MMR adjusted retail value |


Internal Only: If the "**color**" query parameter is used, the "**adjustedBy**" field will contain additional information with one or more of the fields below.  

|Field | Type | Description | 
|---------|----------|----------|
| ColorAdjustmentValue |Object |Information about the amount for which the valuation was adjusted due to the color query parameter|
| ColorAdjustmentValue.wholesale | - |Information about the adjusted wholesale valuation pricing based on the color query parameter |
| ColorAdjustmentValue.wholesale.average |Integer| Average adjusted valuation |
| ColorAdjustmentValue.retail | - |Information about the adjusted retail valuation pricing due to the color query parameter when the retail query parameter was also used |
| ColorAdjustmentValue.retail.average |Integer |Average MMR adjusted retail value |


Internal Only: If the "**grade**" query parameter is used, the "**adjustedBy**" field will contain additional information with one or more of the fields below.  

|Field  | Type | Description |
|-------|-------|--------|
| Grade |Integer | Condition of the vehicle such that "30" is equivalent to "3.0" as displayed in the MMR | 
| GradeAdjustmentValue | Object |Information about the amount for which the valuation was adjusted by grade |
| GradeAdjustmentValue.wholesale | Object | Information about the adjusted wholesale valuation pricing due to the grade passed in the request |
| GradeAdjustmentValue.wholesale.average |Integer| Average adjusted valuation |
| GradeAdjustmentValue.retail | Object | Information about the adjusted retail valuation pricing due to the grade passed in the request when using the "Retail" query parameter |
| GradeAdjustmentValue.retail.average |Integer |Average MMR adjusted retail value |




</private>








<a name="responseExample"></a>



#### Example JSON Response 

The following is an example of the response to a request using only the VIN.

```
{
    "href": "https://integration1.api.manheim.com/valuations/vin/WBA3C1C5XFP853102",
    "count": 1,
    "items": [
        {
            "href": "https://integration1.api.manheim.com/valuations/id/201500600174249?country=US",
            "description": {
                "year": 2015,
                "make": "B M W",
                "model": "3 SERIES",
                "trim": "4D SEDAN 328I SPORT",
                "subSeries": "328I SPT"
            },
            "adjustedPricing": {
                "wholesale": {
                    "above": 21200,
                    "average": 19550,
                    "below": 17900
                },
                "adjustedBy": {}
            },
            "wholesale": {
                "above": 21200,
                "average": 19550,
                "below": 17900
            },
            "averageOdometer": 33610,
            "odometerUnits": "miles",
            "averageGrade": 41,
            "currency": "USD"
        }
    ]
}
```

The following is an example of the response to a request that includes "odometer" in the query string. **Note** that two items are returned, and the "bestMatch" field is present and is set to *true* for one of the items.

```
{
    "href": "https://integration1.api.manheim.com/valuations/vin/WBA3C1C5XFP853102?odometer=20000",
    "count": 2,
    "items": [
        {
            "href": "https://integration1.api.manheim.com/valuations/id/201500600174958?country=US&odometer=20000",
            "description": {
                "year": 2015,
                "make": "B M W",
                "model": "3 SERIES",
                "trim": "4D SEDAN 328I",
                "subSeries": "328I"
            },
            "adjustedPricing": {
                "wholesale": {
                    "above": 20200,
                    "average": 18550,
                    "below": 16900
                },
                "adjustedBy": {
                    "Odometer": "20000"
                }
            },
            "wholesale": {
                "above": 18750,
                "average": 17050,
                "below": 15400
            },
            "averageOdometer": 34889,
            "odometerUnits": "miles",
            "averageGrade": 41,
            "currency": "USD",
            "bestMatch": true
        },
        {
            "href": "https://integration1.api.manheim.com/valuations/id/201500600174249?country=US&odometer=20000",
            "description": {
                "year": 2015,
                "make": "B M W",
                "model": "3 SERIES",
                "trim": "4D SEDAN 328I SPORT",
                "subSeries": "328I SPT"
            },
            "adjustedPricing": {
                "wholesale": {
                    "above": 23000,
                    "average": 21300,
                    "below": 19600
                },
                "adjustedBy": {
                    "Odometer": "20000"
                }
            },
            "wholesale": {
                "above": 21200,
                "average": 19550,
                "below": 17900
            },
            "averageOdometer": 33610,
            "odometerUnits": "miles",
            "averageGrade": 41,
            "currency": "USD"
        }
    ]
}
``` 


<private>

Internal Only: If the "**odometer**" query parameter is used, the "**adjustedBy**" field will contain additional information as shown in this example.  

```
{
    "href": "https://integration1.api.manheim.com/valuations/vin/WBA3C1C5XFP853102?odometer=20000",
    "count": 2,
    "items": [
        {
            "href": "https://integration1.api.manheim.com/valuations/id/201500600174958?country=US&odometer=20000",
            "description": {
                "year": 2015,
                "make": "B M W",
                "model": "3 SERIES",
                "trim": "4D SEDAN 328I",
                "subSeries": "328I"
            },
            "adjustedPricing": {
                "wholesale": {
                    "above": 20200,
                    "average": 18550,
                    "below": 16900
                },
                "adjustedBy": {
                    "Odometer": "20000",
                    "OdometerAdjustmentValue": "1500"
                }
            },
            "wholesale": {
                "above": 18750,
                "average": 17050,
                "below": 15400
            },
            "averageOdometer": 34889,
            "odometerUnits": "miles",
            "averageGrade": 41,
            "currency": "USD",
            "bestMatch": true,
            "samples": {
                "href": "https://integration1.api.manheim.com/valuation-samples/id/201500600174958?country=US&orderBy=location%20desc&start=1&limit=25"
            }
        },
        {
            "href": "https://integration1.api.manheim.com/valuations/id/201500600174249?country=US&odometer=20000",
            "description": {
                "year": 2015,
                "make": "B M W",
                "model": "3 SERIES",
                "trim": "4D SEDAN 328I SPORT",
                "subSeries": "328I SPT"
            },
            "adjustedPricing": {
                "wholesale": {
                    "above": 23000,
                    "average": 21300,
                    "below": 19600
                },
                "adjustedBy": {
                    "Odometer": "20000",
                    "OdometerAdjustmentValue": "1730"
                }
            },
            "wholesale": {
                "above": 21200,
                "average": 19550,
                "below": 17900
            },
            "averageOdometer": 33610,
            "odometerUnits": "miles",
            "averageGrade": 41,
            "currency": "USD",
            "samples": {
                "href": "https://integration1.api.manheim.com/valuation-samples/id/201500600174249?country=US&orderBy=location%20desc&start=1&limit=25"
            }
        }
    ]
}
``` 

</private>




The following is an example of the response to a request that includes "odometer", "region", and "include=retail,forecast,historical" in the query string. 

```
{
    "href": "https://integration1.api.manheim.com/valuations/vin/WBA3C1C5XFP853102?odometer=20000&region=NE&include=retail%2Chistorical%2Cforecast",
    "count": 2,
    "items": [
        {
            "href": "https://integration1.api.manheim.com/valuations/id/201500600174958?country=US&odometer=20000&region=NE&include=retail,historical,forecast",
            "description": {
                "year": 2015,
                "make": "B M W",
                "model": "3 SERIES",
                "trim": "4D SEDAN 328I",
                "subSeries": "328I"
            },
            "adjustedPricing": {
                "wholesale": {
                    "above": 20200,
                    "average": 18550,
                    "below": 16900
                },
                "retail": {
                    "above": 24700,
                    "average": 22900,
                    "below": 21100
                },
                "adjustedBy": {
                    "Odometer": "20000",
                    "Region": "NE"
                }
            },
            "wholesale": {
                "above": 18750,
                "average": 17050,
                "below": 15400
            },
            "retail": {
                "above": 23200,
                "average": 21400,
                "below": 19650
            },
            "historicalAverages": {
                "last30Days": {
                    "odometer": 34889,
                    "price": 17250
                },
                "lastMonth": {
                    "odometer": 34925,
                    "price": 17550
                },
                "lastTwoMonths": {
                    "odometer": 33362,
                    "price": 18000
                },
                "lastSixMonths": {
                    "odometer": 37774,
                    "price": 18250
                },
                "lastYear": {
                    "odometer": 30623,
                    "price": 19750
                }
            },
            "forecast": {
                "nextMonth": {
                    "wholesale": 16800,
                    "retail": 21100
                },
                "nextYear": {
                    "wholesale": 14150,
                    "retail": 18250
                }
            },
            "averageOdometer": 34889,
            "odometerUnits": "miles",
            "averageGrade": 41,
            "currency": "USD",
            "bestMatch": true
        },
        {
            "href": "https://integration1.api.manheim.com/valuations/id/201500600174249?country=US&odometer=20000&region=NE&include=retail,historical,forecast",
            "description": {
                "year": 2015,
                "make": "B M W",
                "model": "3 SERIES",
                "trim": "4D SEDAN 328I SPORT",
                "subSeries": "328I SPT"
            },
            "adjustedPricing": {
                "wholesale": {
                    "above": 22900,
                    "average": 21300,
                    "below": 19600
                },
                "retail": {
                    "above": 27500,
                    "average": 25800,
                    "below": 24000
                },
                "adjustedBy": {
                    "Odometer": "20000",
                    "Region": "NE"
                }
            },
            "wholesale": {
                "above": 21200,
                "average": 19550,
                "below": 17900
            },
            "retail": {
                "above": 25800,
                "average": 24100,
                "below": 22300
            },
            "historicalAverages": {
                "last30Days": {
                    "odometer": 33610,
                    "price": 19400
                },
                "lastMonth": {
                    "odometer": 32225,
                    "price": 19250
                },
                "lastTwoMonths": {
                    "odometer": 34115,
                    "price": 19350
                },
                "lastSixMonths": {
                    "odometer": 37422,
                    "price": 20200
                },
                "lastYear": {
                    "odometer": 21333,
                    "price": 24100
                }
            },
            "forecast": {
                "nextMonth": {
                    "wholesale": 19800,
                    "retail": 24300
                },
                "nextYear": {
                    "wholesale": 15900,
                    "retail": 20100
                }
            },
            "averageOdometer": 33610,
            "odometerUnits": "miles",
            "averageGrade": 41,
            "currency": "USD"
        }
    ]
}
```


<private>

Internal Only: The following is an example of the response to a request that includes "odometer", "region", and "include=retail,forecast,historical" in the query string. Internal customers will see the "**adjustedBy**" field containing adjusted values for odometer and region, as shown in this example.  

```
{
    "href": "https://integration1.api.manheim.com/valuations/vin/WBA3C1C5XFP853102?odometer=20000&region=NE&include=retail%2Chistorical%2Cforecast",
    "count": 2,
    "items": [
        {
            "href": "https://integration1.api.manheim.com/valuations/id/201500600174958?country=US&odometer=20000&region=NE&include=retail,historical,forecast",
            "description": {
                "year": 2015,
                "make": "B M W",
                "model": "3 SERIES",
                "trim": "4D SEDAN 328I",
                "subSeries": "328I"
            },
            "adjustedPricing": {
                "wholesale": {
                    "above": 20200,
                    "average": 18550,
                    "below": 16900
                },
                "retail": {
                    "above": 24700,
                    "average": 22900,
                    "below": 21100
                },
                "adjustedBy": {
                    "Odometer": "20000",
                    "OdometerAdjustmentValue": "1500",
                    "Region": "NE",
                    "RegionAdjustmentValue": {
                        "wholesale": {
                            "above": 0,
                            "average": 0,
                            "below": 0
                        },
                        "retail": {
                            "above": -10,
                            "average": -10,
                            "below": 0
                        }
                    }
                }
            },
            "wholesale": {
                "above": 18750,
                "average": 17050,
                "below": 15400
            },
            "retail": {
                "above": 23200,
                "average": 21400,
                "below": 19650
            },
            "historicalAverages": {
                "last30Days": {
                    "odometer": 34889,
                    "price": 17250
                },
                "lastMonth": {
                    "odometer": 34925,
                    "price": 17550
                },
                "lastTwoMonths": {
                    "odometer": 33362,
                    "price": 18000
                },
                "lastSixMonths": {
                    "odometer": 37774,
                    "price": 18250
                },
                "lastYear": {
                    "odometer": 30623,
                    "price": 19750
                }
            },
            "forecast": {
                "nextMonth": {
                    "wholesale": 16800,
                    "retail": 21100
                },
                "nextYear": {
                    "wholesale": 14150,
                    "retail": 18250
                }
            },
            "averageOdometer": 34889,
            "odometerUnits": "miles",
            "averageGrade": 41,
            "currency": "USD",
            "bestMatch": true,
            "samples": {
                "href": "https://integration1.api.manheim.com/valuation-samples/id/201500600174958?country=US&orderBy=location%20desc&start=1&limit=25"
            }
        },
        {
            "href": "https://integration1.api.manheim.com/valuations/id/201500600174249?country=US&odometer=20000&region=NE&include=retail,historical,forecast",
            "description": {
                "year": 2015,
                "make": "B M W",
                "model": "3 SERIES",
                "trim": "4D SEDAN 328I SPORT",
                "subSeries": "328I SPT"
            },
            "adjustedPricing": {
                "wholesale": {
                    "above": 22900,
                    "average": 21300,
                    "below": 19600
                },
                "retail": {
                    "above": 27500,
                    "average": 25800,
                    "below": 24000
                },
                "adjustedBy": {
                    "Odometer": "20000",
                    "OdometerAdjustmentValue": "1730",
                    "Region": "NE",
                    "RegionAdjustmentValue": {
                        "wholesale": {
                            "above": -20,
                            "average": -20,
                            "below": -10
                        },
                        "retail": {
                            "above": -20,
                            "average": -20,
                            "below": -20
                        }
                    }
                }
            },
            "wholesale": {
                "above": 21200,
                "average": 19550,
                "below": 17900
            },
            "retail": {
                "above": 25800,
                "average": 24100,
                "below": 22300
            },
            "historicalAverages": {
                "last30Days": {
                    "odometer": 33610,
                    "price": 19400
                },
                "lastMonth": {
                    "odometer": 32225,
                    "price": 19250
                },
                "lastTwoMonths": {
                    "odometer": 34115,
                    "price": 19350
                },
                "lastSixMonths": {
                    "odometer": 37422,
                    "price": 20200
                },
                "lastYear": {
                    "odometer": 21333,
                    "price": 24100
                }
            },
            "forecast": {
                "nextMonth": {
                    "wholesale": 19800,
                    "retail": 24300
                },
                "nextYear": {
                    "wholesale": 15900,
                    "retail": 20100
                }
            },
            "averageOdometer": 33610,
            "odometerUnits": "miles",
            "averageGrade": 41,
            "currency": "USD",
            "samples": {
                "href": "https://integration1.api.manheim.com/valuation-samples/id/201500600174249?country=US&orderBy=location%20desc&start=1&limit=25"
            }
        }
    ]
}
```

</private>


The API will return a response similar to the following if the request includes "odometer", "region", "color", "grade", and "include=retail,historical,forecast" in the query string. 


```
{
    "href": "https://integration1.api.manheim.com/valuations/vin/WBA3C1C5XFP853102?color=WHITE&grade=31&odometer=20000&region=NE&include=retail%2Chistorical%2Cforecast",
    "count": 2,
    "items": [
        {
            "href": "https://integration1.api.manheim.com/valuations/id/201500600174958?country=US&odometer=20000&region=NE&color=WHITE&grade=31&include=retail,historical,forecast",
            "description": {
                "year": 2015,
                "make": "B M W",
                "model": "3 SERIES",
                "trim": "4D SEDAN 328I",
                "subSeries": "328I"
            },
            "adjustedPricing": {
                "wholesale": {
                    "above": 19550,
                    "average": 17950,
                    "below": 16300
                },
                "retail": {
                    "above": 23800,
                    "average": 22100,
                    "below": 20400
                },
                "adjustedBy": {
                    "Color": "WHITE",
                    "Grade": "31",
                    "Odometer": "20000",
                    "Region": "NE"
                }
            },
            "wholesale": {
                "above": 18750,
                "average": 17050,
                "below": 15400
            },
            "retail": {
                "above": 23200,
                "average": 21400,
                "below": 19650
            },
            "historicalAverages": {
                "last30Days": {
                    "odometer": 34889,
                    "price": 17250
                },
                "lastMonth": {
                    "odometer": 34925,
                    "price": 17550
                },
                "lastTwoMonths": {
                    "odometer": 33362,
                    "price": 18000
                },
                "lastSixMonths": {
                    "odometer": 37774,
                    "price": 18250
                },
                "lastYear": {
                    "odometer": 30623,
                    "price": 19750
                }
            },
            "forecast": {
                "nextMonth": {
                    "wholesale": 16800,
                    "retail": 21100
                },
                "nextYear": {
                    "wholesale": 14150,
                    "retail": 18250
                }
            },
            "averageOdometer": 34889,
            "odometerUnits": "miles",
            "averageGrade": 41,
            "currency": "USD",
            "bestMatch": true
        },
        {
            "href": "https://integration1.api.manheim.com/valuations/id/201500600174249?country=US&odometer=20000&region=NE&color=WHITE&grade=31&include=retail,historical,forecast",
            "description": {
                "year": 2015,
                "make": "B M W",
                "model": "3 SERIES",
                "trim": "4D SEDAN 328I SPORT",
                "subSeries": "328I SPT"
            },
            "adjustedPricing": {
                "wholesale": {
                    "above": 22200,
                    "average": 20500,
                    "below": 18900
                },
                "retail": {
                    "above": 26600,
                    "average": 24900,
                    "below": 23100
                },
                "adjustedBy": {
                    "Color": "WHITE",
                    "Grade": "31",
                    "Odometer": "20000",
                    "Region": "NE"
                }
            },
            "wholesale": {
                "above": 21200,
                "average": 19550,
                "below": 17900
            },
            "retail": {
                "above": 25800,
                "average": 24100,
                "below": 22300
            },
            "historicalAverages": {
                "last30Days": {
                    "odometer": 33610,
                    "price": 19400
                },
                "lastMonth": {
                    "odometer": 32225,
                    "price": 19250
                },
                "lastTwoMonths": {
                    "odometer": 34115,
                    "price": 19350
                },
                "lastSixMonths": {
                    "odometer": 37422,
                    "price": 20200
                },
                "lastYear": {
                    "odometer": 21333,
                    "price": 24100
                }
            },
            "forecast": {
                "nextMonth": {
                    "wholesale": 19800,
                    "retail": 24300
                },
                "nextYear": {
                    "wholesale": 15900,
                    "retail": 20100
                }
            },
            "averageOdometer": 33610,
            "odometerUnits": "miles",
            "averageGrade": 41,
            "currency": "USD"
        }
    ]
}
```




<private> 



<a name="internalResponseWithMultipleParameters"></a>


Internal Only: Internal users would see an a response similar to the following if the API request includes "odometer", "region", "color", "grade" and "include=retail,historical,forecast" in the query string. 


```
{
    "href": "https://integration1.api.manheim.com/valuations/vin/WBA3C1C5XFP853102?color=WHITE&grade=31&odometer=20000&region=NE&include=retail%2Chistorical%2Cforecast",
    "count": 2,
    "items": [
        {
            "href": "https://integration1.api.manheim.com/valuations/id/201500600174958?country=US&odometer=20000&region=NE&color=WHITE&grade=31&include=retail,historical,forecast",
            "description": {
                "year": 2015,
                "make": "B M W",
                "model": "3 SERIES",
                "trim": "4D SEDAN 328I",
                "subSeries": "328I"
            },
            "adjustedPricing": {
                "wholesale": {
                    "above": 19550,
                    "average": 17950,
                    "below": 16300
                },
                "retail": {
                    "above": 23800,
                    "average": 22100,
                    "below": 20400
                },
                "adjustedBy": {
                    "Color": "WHITE",
                    "ColorAdjustmentValue": {
                        "wholesale": {
                            "above": 120,
                            "average": 110,
                            "below": 100
                        },
                        "retail": {
                            "above": 140,
                            "average": 130,
                            "below": 120
                        }
                    },
                    "Grade": "31",
                    "GradeAdjustmentValue": {
                        "wholesale": {
                            "above": -790,
                            "average": -720,
                            "below": -650
                        },
                        "retail": {
                            "above": -960,
                            "average": -890,
                            "below": -820
                        }
                    },
                    "Odometer": "20000",
                    "OdometerAdjustmentValue": "1500",
                    "Region": "NE",
                    "RegionAdjustmentValue": {
                        "wholesale": {
                            "above": 0,
                            "average": 0,
                            "below": 0
                        },
                        "retail": {
                            "above": -10,
                            "average": -10,
                            "below": 0
                        }
                    }
                }
            },
            "wholesale": {
                "above": 18750,
                "average": 17050,
                "below": 15400
            },
            "retail": {
                "above": 23200,
                "average": 21400,
                "below": 19650
            },
            "historicalAverages": {
                "last30Days": {
                    "odometer": 34889,
                    "price": 17250
                },
                "lastMonth": {
                    "odometer": 34925,
                    "price": 17550
                },
                "lastTwoMonths": {
                    "odometer": 33362,
                    "price": 18000
                },
                "lastSixMonths": {
                    "odometer": 37774,
                    "price": 18250
                },
                "lastYear": {
                    "odometer": 30623,
                    "price": 19750
                }
            },
            "forecast": {
                "nextMonth": {
                    "wholesale": 16800,
                    "retail": 21100
                },
                "nextYear": {
                    "wholesale": 14150,
                    "retail": 18250
                }
            },
            "averageOdometer": 34889,
            "odometerUnits": "miles",
            "averageGrade": 41,
            "currency": "USD",
            "bestMatch": true,
            "samples": {
                "href": "https://integration1.api.manheim.com/valuation-samples/id/201500600174958?country=US&orderBy=location%20desc&start=1&limit=25"
            }
        },
        {
            "href": "https://integration1.api.manheim.com/valuations/id/201500600174249?country=US&odometer=20000&region=NE&color=WHITE&grade=31&include=retail,historical,forecast",
            "description": {
                "year": 2015,
                "make": "B M W",
                "model": "3 SERIES",
                "trim": "4D SEDAN 328I SPORT",
                "subSeries": "328I SPT"
            },
            "adjustedPricing": {
                "wholesale": {
                    "above": 22200,
                    "average": 20500,
                    "below": 18900
                },
                "retail": {
                    "above": 26600,
                    "average": 24900,
                    "below": 23100
                },
                "adjustedBy": {
                    "Color": "WHITE",
                    "ColorAdjustmentValue": {
                        "wholesale": {
                            "above": 110,
                            "average": 100,
                            "below": 100
                        },
                        "retail": {
                            "above": 140,
                            "average": 130,
                            "below": 120
                        }
                    },
                    "Grade": "31",
                    "GradeAdjustmentValue": {
                        "wholesale": {
                            "above": -890,
                            "average": -830,
                            "below": -760
                        },
                        "retail": {
                            "above": -1070,
                            "average": -1000,
                            "below": -930
                        }
                    },
                    "Odometer": "20000",
                    "OdometerAdjustmentValue": "1730",
                    "Region": "NE",
                    "RegionAdjustmentValue": {
                        "wholesale": {
                            "above": -20,
                            "average": -20,
                            "below": -10
                        },
                        "retail": {
                            "above": -20,
                            "average": -20,
                            "below": -20
                        }
                    }
                }
            },
            "wholesale": {
                "above": 21200,
                "average": 19550,
                "below": 17900
            },
            "retail": {
                "above": 25800,
                "average": 24100,
                "below": 22300
            },
            "historicalAverages": {
                "last30Days": {
                    "odometer": 33610,
                    "price": 19400
                },
                "lastMonth": {
                    "odometer": 32225,
                    "price": 19250
                },
                "lastTwoMonths": {
                    "odometer": 34115,
                    "price": 19350
                },
                "lastSixMonths": {
                    "odometer": 37422,
                    "price": 20200
                },
                "lastYear": {
                    "odometer": 21333,
                    "price": 24100
                }
            },
            "forecast": {
                "nextMonth": {
                    "wholesale": 19800,
                    "retail": 24300
                },
                "nextYear": {
                    "wholesale": 15900,
                    "retail": 20100
                }
            },
            "averageOdometer": 33610,
            "odometerUnits": "miles",
            "averageGrade": 41,
            "currency": "USD",
            "samples": {
                "href": "https://integration1.api.manheim.com/valuation-samples/id/201500600174249?country=US&orderBy=location%20desc&start=1&limit=25"
            }
        }
    ]
}
```



</private> 






<a name="responseMapToMMR"></a>

### How API Response Parameters Map to the Manheim Market Report
This section describe how the Valuations API response fields correlate with the fields in the Manheim Market Report screens. 

Note: Each of the Valuations API response parameters listed in the following tables is contained in a valuations object in the **items** array.





<private>




See **[this example](/#/apis/marketplace/valuations#internalResponseWithMultipleParameters  "Internal response with multiple parameters")** of a response to an internal request that shows all of the described response parameters.




</private>



<img src="img/misc/mmr_to_valuations_map_mmr_header.d7bc96c8.png" alt="Valuations API to MMR - header" height="213" width="800"/>



|Item # | Valuations Response Parameter  | 
|-------|-------------------------------------------------------|
| 1     |  description.year |
| 2     |  description.make |
| 3     |  description.model |
| 4     |  description.trim |



---



<img src="img/misc/mmr_to_valuations_map-mmr.d35bc74c.png" alt="Valuations API to MMR - MMR" height="229" width="784"/>

<br>

| Item # | Valuations Response Parameter            | 
|-------|------------------------------------------------|
| 1     |  wholesale.average |
| 2     |  averageOdometer |
| 3     |  averageGrade |
| 4     |  wholesale.below |
| 5     |  wholesale.above |
| 6     |  adjustedPricing.adjustedBy.Odometer |
| 7     |  adjustedPricing.adjustedBy.Region |
| 8     |  adjustedPricing.adjustedBy.Grade |
| 9     |  adjustedPricing.adjustedBy.Color |
| 10    |  adjustedPricing.wholesale.average |
| 11    |  wholesale.below |
| 12    |  wholesale.average |
| 13    |  wholesale.above |





<private>




For internal API users, if the odometer, region, grade, and/or color parameters are passed in the request, the API response includes adjustment details for each, as shown in the following image and table.

<img src="img/misc/mmr_to_valuations_map-mmr_int.04b269dd.png" alt="Valuations API to MMR - MMR" height="229" width="782"/>



| Item # | Valuations Response Parameter            | 
|-------|------------------------------------------------|
| 14    |  adjustedBy.OdometerAdjustedValue.wholesale.average |
| 15    |  adjustedBy.RegionAdjustmentValue.wholesale.average |
| 16    |  adjustedBy.GradeAdjustmentValue.wholesale.average |
| 17    |  adjustedBy.ColorAdjustmentValue.wholesale.average |





</private>



<br>

---

<img src="img/misc/mmr_to_valuations_map_mmr_ave_est_.34266455.png" alt="Valuations API to MMR - Average - Estimates" height="353" width="620"/>


|Item # | Valuations Response Parameter                         | 
|-------|-------------------------------------------------------|
| 1     |  historicalAverages.last30Days.price |
| 2     |  historicalAverages.last30Days.odometer |
| 3     |  historicalAverages.lastSixMonths.price |
| 4     |  historicalAverages.lastSixMonths.odometer |
| 5     |  historicalAverages.lastYear.price |
| 6     |  historicalAverages.lastYear.odometer |
| 7     |  forecast.nextMonth.wholesale |
| 8     |  adjustedPricing.retail.average |
| 9     |  retail.below |
| 10    |  retail.above |









<a name="retrieveValuationsByMID"></a>



### Retrieve Valuations by MID

#### Endpoint

```
GET https://integration1.api.manheim.com/valuations/id/MID
```


#### Description

This method allows a user to use the 15 or 16 digit Manheim ID (MID) to retrieve valuations. 

#### Common Return Codes 

|Response Code | Response Message | Possible Next Actions | 
|--------------|------------------|------------------------|
|200 OK   | Body contains the requested information | Successful response; no actions necessary |
|400 Bad Request | **ERROR:** Invalid ID | MID may contain invalid characters or may be the wrong length; check and resubmit |
|401 Unauthorized |**ERROR:** Developer inactive | API token may be malformed or the user does not have access; check the token or contact Manheim for further support |
|404 Not Found | **ERROR:** Matching vehicles not found | URL may be malformed or the requested valuation does not exist; check and resubmit |
|500 Server Error | **ERROR:** Unknown Error | Resubmit the request; if issue still exists contact Manheim for support |
|596 596 | **ERROR:** 596 Service Not Found | URL may be malformed; check the method name and resubmit |


#### Request Parameters 

This method requires the MID in the URL. 

The query parameters for the method to ["Retrieve Valuations by VIN"](/#/apis/marketplace/valuations#queryParameters "Query Parameters") apply to this method.


#### Example JSON Request

The **ID** at the end of the URL should be replaced with the **unique** Manheim ID (MID), as shown in the example below.

```
GET https://integration1.api.manheim.com/valuations/id/200605335240007
```


The URL may also contain a query string similar to the following. 

```
GET https://integration1.api.manheim.com/valuations/id/200605335240007?odometer=10000&region=se&include=retail
```



The query string may also include additional parameters for "color" and "grade" similar to the following. 

```
GET https://integration1.api.manheim.com/valuations/id/201401269414434?color=WHITE&grade=31&odometer=20000&region=NE
```






#### Response Parameters 

This method returns the same fields as the method to [Retrieve Valuations by VIN](/#/apis/marketplace/valuations#responseFields "Response Fields").




#### Example JSON Response 

This method returns a similar response to the method ["Retrieve Valuations by VIN"](/#/apis/marketplace/valuations#responseExample "Example Responses").


The following example shows a response to a query that includes multiple parameters, as shown the "href" fields in the response.

```
{
    "href": "https://integration1.api.manheim.com/valuations/id/201308559801684?region=SE&odometer=60500&color=BLUE&grade=45&include=retail,historical,forecast",
    "count": 1,
    "items": [
        {
            "href": "https://integration1.api.manheim.com/valuations/id/201308559801684?country=US&odometer=60500&region=SE&color=BLUE&grade=45&include=retail,historical,forecast",
            "description": {
                "year": 2013,
                "make": "KIA",
                "model": "SPORTAGE FWD",
                "trim": "4D SUV 2.4L",
                "subSeries": "BASE"
            },
            "adjustedPricing": {
                "wholesale": {
                    "average": 11250
                },
                "retail": {
                    "average": 15400
                },
                "adjustedBy": {
                    "Color": "BLUE",
                    "Grade": "45",
                    "Odometer": "60500",
                    "Region": "SE"
                }
            },
            "wholesale": {
                "above": 10500,
                "average": 8900,
                "below": 7300
            },
            "retail": {
                "above": 14100,
                "average": 12500,
                "below": 10950
            },
            "historicalAverages": {
                "last30Days": {
                    "odometer": 72732,
                    "price": 8925
                },
                "lastMonth": {
                    "odometer": 51316,
                    "price": 10050
                },
                "lastTwoMonths": {
                    "odometer": 93240,
                    "price": 8200
                },
                "lastSixMonths": {
                    "odometer": 44560,
                    "price": 11800
                },
                "lastYear": {
                    "odometer": 42076,
                    "price": 12050
                }
            },
            "forecast": {
                "nextMonth": {
                    "wholesale": 8850,
                    "retail": 12450
                },
                "nextYear": {
                    "wholesale": 8050,
                    "retail": 11650
                }
            },
            "averageOdometer": 72732,
            "odometerUnits": "miles",
            "averageGrade": 22,
            "currency": "USD"
        }
    ]
}
```




<private> 



Internal Only: The following response example displays fields only available to internal users. The query includes multiple parameters, which are shown in the "href" values in the response.


```
{
    "href": "https://integration1.api.manheim.com/valuations/id/201308559801684?region=SE&odometer=60500&color=BLUE&grade=45&include=retail%252Chistorical%252Cforecast",
    "count": 1,
    "items": [
        {
            "href": "https://integration1.api.manheim.com/valuations/id/201308559801684?country=US&odometer=60500&region=SE&color=BLUE&grade=45&include=retail,historical,forecast",
            "description": {
                "year": 2013,
                "make": "KIA",
                "model": "SPORTAGE FWD",
                "trim": "4D SUV 2.4L",
                "subSeries": "BASE"
            },
            "adjustedPricing": {
                "wholesale": {
                    "average": 11250
                },
                "retail": {
                    "average": 15400
                },
                "adjustedBy": {
                    "Color": "BLUE",
                    "ColorAdjustmentValue": {
                        "wholesale": {
                            "average": 100
                        },
                        "retail": {
                            "average": 140
                        }
                    },
                    "Grade": "45",
                    "GradeAdjustmentValue": {
                        "wholesale": {
                            "average": 1280
                        },
                        "retail": {
                            "average": 1750
                        }
                    },
                    "Odometer": "60500",
                    "OdometerAdjustmentValue": "910",
                    "Region": "SE",
                    "RegionAdjustmentValue": {
                        "wholesale": {
                            "average": 80
                        },
                        "retail": {
                            "average": 100
                        }
                    }
                }
            },
            "wholesale": {
                "above": 10500,
                "average": 8900,
                "below": 7300
            },
            "retail": {
                "above": 14100,
                "average": 12500,
                "below": 10950
            },
            "historicalAverages": {
                "last30Days": {
                    "odometer": 72732,
                    "price": 8925
                },
                "lastMonth": {
                    "odometer": 51316,
                    "price": 10050
                },
                "lastTwoMonths": {
                    "odometer": 93240,
                    "price": 8200
                },
                "lastSixMonths": {
                    "odometer": 44560,
                    "price": 11800
                },
                "lastYear": {
                    "odometer": 42076,
                    "price": 12050
                }
            },
            "forecast": {
                "nextMonth": {
                    "wholesale": 8850,
                    "retail": 12450
                },
                "nextYear": {
                    "wholesale": 8050,
                    "retail": 11650
                }
            },
            "averageOdometer": 72732,
            "odometerUnits": "miles",
            "averageGrade": 22,
            "currency": "USD"
        }
    ],
    "samples": {
        "href": "https://integration1.api.manheim.com/valuation-samples/id/201308559801684?country=US&orderBy=location%20desc&start=1&limit=25"
    }
}
```




</private>





<a name="searchValuations"></a>


###  Search Valuations 

#### Endpoints

```
GET https://integration1.api.manheim.com/valuations/search/YEAR/MAKE

GET https://integration1.api.manheim.com/valuations/search/YEAR/MAKE/MODEL

GET https://integration1.api.manheim.com/valuations/search/YEAR/MAKE/MODEL/TRIM
```


#### Description 

This method allows a user to retrieve valuations based on details of a vehicle, such as the year, make, model or trim.  

#### Common Return Codes  

|Response Code | Response Message | Possible Next Actions |
|--------------|------------------|-----------------------|
|200 OK | Body contains the requested information | Successful response; no actions necessary |
|401 Unauthorized | **ERROR:** Developer inactive | API token may be malformed or the user does not have access; check the token or contact Manheim for further support |
|404 Not Found | **ERROR:** Matching vehicles not found | URL method or search parameters may be malformed; check and resubmit |
|500 Server Error | **ERROR:** Unknown Error | Resubmit the request; if issue still exists contact Manheim for support |
|596 596 | **ERROR:** Service Not Found | URL may be malformed; check the method name and resubmit | 



#### Request Parameters

This method requires certain parameters in the URL as described in the table below. 

|Parameter | Type | Requirement |Description |
|----------|--------|------------|------------|
|YEAR      |Integer| REQUIRED | Year of the vehicle |
|MAKE      |String | REQUIRED | Make of the vehicle |
|MODEL     |String | REQUIRED if "TRIM" is present | Model of the vehicle, partial or whole | 
|TRIM      |String | OPTIONAL | Trim style of the vehicle, partial or whole | 


The query parameters for the method to ["Retrieve Valuations by VIN"](/#/apis/marketplace/valuations#queryParameters "Query Parameters") apply to this method.


#### Example JSON Requests


The "YEAR" and "MAKE" in the URL above would be replaced by the year and make of the vehicle similar to the following example.

```
GET https://integration1.api.manheim.com/valuations/search/2009/honda
```

The user may filter the results further by replacing "MODEL" in the URL above with a whole or partial model of a vehicle to retrieve valuations.

```
GET https://integration1.api.manheim.com/valuations/search/2009/honda/accordv6
```

The user may filter the year, make and model by replacing "TRIM" in the URL above with a specific whole or partial trim value, similar to the example below.

```
GET https://integration1.api.manheim.com/valuations/search/2009/honda/accordv6/sedan
```

The user may add an optional query string similar to the other methods above and in the following example. 

```
GET https://integration1.api.manheim.com/valuations/search/2009/honda/accordv6/sedan?region=SE&include=historical
``` 



The query may also contain *color* and *grade* parameters as shown in the following example. 

```
GET `https://integration1.api.manheim.com/valuations/search/2009/honda/accordv6/sedan?color=red&grade=40`
```



#### Response Parameters 

This method returns the same fields as the method to [Retrieve Valuations by VIN](/#/apis/marketplace/valuations#responseFields "Response Fields").

#### Example JSON Response 

This method returns a similar response to the method ["Retrieve Valuations by VIN"](/#/apis/marketplace/valuations#responseExample "Example Responses").





### Retrieve All Colors 

#### Endpoint 

```
GET https://integration1.api.manheim.com/valuations/colors
```


#### Description 

This method allows an API user to retrieve all of the colors that may be used as a query parameter to obtain color-adjusted valuations. See ["Retrieve Valuations by VIN"](/#/apis/marketplace/valuations#retrieveValuationsByVIN  "Valuations API") for more information.



#### Common Return Codes

|Response Code | Response Message | Possible Next Actions |
|--------------|------------------|---------------------|
|200 OK        | Body contains the requested information | Successful response; no actions necessary |
|401 Unauthorized | **ERROR:** Developer inactive | API token may be malformed or the user does not have access; check the token or contact Manheim for further support |
|404 Not Found    | **ERROR:** HTML response may contain details about the error | URL may be malformed; check and resubmit |
|500 Server Error | **ERROR:** Unknown Error | Resubmit the request; if issue still exists contact Manheim for support |



#### Example JSON Request

The following shows an example of the request using a query string parameter. 

```
GET https://integration1.api.manheim.com/valuations/colors
```


#### Response Parameters

The overall JSON response for this method contains the following fields.


|Field    | Type   | Description | 
|---------|--------|--------------|
|href    | String | URL of the request |
|count    |Integer | Number of colors returned |
|**items**| Array | Array containing an item object for each color; the number of items matches the value of the "count" field. Each item contains a color value as a string.  |


Each color is described by the *value* field: 

|Field     | Type | Description | 
|-------------|---------|--------------|
| value | String | Unique name for a color that may be applied to a vehicle in a valuation |




#### Example JSON Response

```
{
    "href": "https://integration1.api.manheim.com/valuations/colors",
    "count": 18,
    "items": [
        {
            "value": "Beige"
        },
        {
            "value": "Black"
        },
        {
            "value": "Blue"
        },
        {
            "value": "Brown"
        },
        {
            "value": "Burgundy"
        },
        {
            "value": "Charcoal"
        },
        {
            "value": "Gold"
        },
        {
            "value": "Gray"
        },
        {
            "value": "Green"
        },
        {
            "value": "Off-white"
        },
        {
            "value": "Orange"
        },
        {
            "value": "Pink"
        },
        {
            "value": "Purple"
        },
        {
            "value": "Red"
        },
        {
            "value": "Silver"
        },
        {
            "value": "Turquoise"
        },
        {
            "value": "White"
        },
        {
            "value": "Yellow"
        }
    ]
}
}
```




### Retrieve All Grades 

#### Endpoint 

```
GET https://integration1.api.manheim.com/valuations/grades
```


#### Description 

This method allows an API user to retrieve all of the condition grades that may be used as a query parameter to obtain grade-adjusted valuations. See ["Retrieve Valuations by VIN"](/#/apis/marketplace/valuations#retrieveValuationsByVIN  "Valuations API") for more information.



#### Common Return Codes

|Response Code | Response Message | Possible Next Actions |
|--------------|------------------|---------------------|
|200 OK        | Body contains the requested information | Successful response; no actions necessary |
|401 Unauthorized | **ERROR:** Developer inactive | API token may be malformed or the user does not have access; check the token or contact Manheim for further support |
|404 Not Found    | **ERROR:** HTML response may contain details about the error | URL may be malformed; check and resubmit |
|500 Server Error | **ERROR:** Unknown Error | Resubmit the request; if issue still exists contact Manheim for support |



#### Example JSON Request

The following shows an example of the request using a query string parameter. 

```
GET https://integration1.api.manheim.com/valuations/grades
```


#### Response Parameters

The overall JSON response for this method contains the following fields.


|Field    | Type   | Description | 
|---------|--------|--------------|
|href    | String | URL of the request |
|count    |Integer | Number of grades returned |
|**items**| Array | Array containing an item object for each grade; the number of items matches the value of the "count" field. Each item contains a grade value as a string |


Each grade item is described by a *value* field: 

|Field     | Type | Description | 
|-------------|---------|--------------|
| value | String | Value for a grade that may be assigned to a vehicle in a valuation. Note that grades are provided as whole numbers; a value of "28" is equivalent to "2.8" |



#### Example JSON Response

```
{
    "href": "https://integration1.api.manheim.com/valuations/grades",
    "count": 32,
    "items": [
        {
            "value": "19"
        },
        {
            "value": "20"
        },
        {
            "value": "21"
        },
        {
            "value": "22"
        },
        {
            "value": "23"
        },
        {
            "value": "24"
        },
        {
            "value": "25"
        },
        {
            "value": "26"
        },
        {
            "value": "27"
        },
        {
            "value": "28"
        },
        {
            "value": "29"
        },
        {
            "value": "30"
        },
        {
            "value": "31"
        },
        {
            "value": "32"
        },
        {
            "value": "33"
        },
        {
            "value": "34"
        },
        {
            "value": "35"
        },
        {
            "value": "36"
        },
        {
            "value": "37"
        },
        {
            "value": "38"
        },
        {
            "value": "39"
        },
        {
            "value": "40"
        },
        {
            "value": "41"
        },
        {
            "value": "42"
        },
        {
            "value": "43"
        },
        {
            "value": "44"
        },
        {
            "value": "45"
        },
        {
            "value": "46"
        },
        {
            "value": "47"
        },
        {
            "value": "48"
        },
        {
            "value": "49"
        },
        {
            "value": "50"
        }
    ]
}
```




<a name="retrieveEditionInfo"></a>


### Retrieve MMR Edition Information

#### Endpoint

```
GET https://integration1.api.manheim.com/valuations/edition
```


#### Description 

This method allows a user to check the current edition of the MMR valuations. The edition reflects the most recent update of Manheim Market Report data for the **Valuations** API. Edition information is available for the United States and Canada. If "date" or "edition" is less than today's date, the data has yet to be refreshed. As noted above, the Manheim Market Report data is refreshed nightly. 


#### Common Return Codes

|Response Code | Response Message | Possible Next Actions |
|----------------|----------------|----------------------|
|200 OK           | Body contains the requested information | Successful response; no actions necessary |
|401 Unauthorized | **ERROR:** Developer inactive | API token may be malformed or the user does not have access; check the token or contact Manheim for further support |
|404 Not Found    | **ERROR:** HTML response may contain details about the error | URL may be malformed; check and resubmit | 
|500 Server Error | **ERROR:** Unknown Error | Resubmit the request; if issue still exists contact Manheim for support |



#### Request Parameters 

This method only allows the following OPTIONAL query string parameters. 

| Parameter | Type | Description |
|-----------|-------|------------|
| country   | String| API calls will default to US if this parameter is omitted; accepted values: US for United States, CA for CANADA |



#### Example JSON Request

The following is an example with a query string to retrieve the edition for Canadian valuations. 

```
GET https://integration1.api.manheim.com/valuations/edition?country=CA
```


#### Response Parameters

The overall JSON response for edition information has the following fields.

| Field | Type       | Notes | 
| ------|---------------- | ----- |
| href  |String| URL of the request |
| count |Integer| Number of editions returned, typically with the value of "1" |
| items | - |Contains one or more blocks of edition information; each item of edition information has the fields listed in the table below, and the number of edition items matches the value of the "count" field |



Each edition item within the JSON object has the following fields.

| Field          |Type            | Notes | 
| ---------------|---------- | ----- |
| date           |Date| Publication date in YYYY-MM-DD format |
| monthAndDay    |String| Publication date's month and day, in "Month DD" format |
| nextMonth      |String| Month and year for next month's publication, in "Month YYYY" format |
| nextYear       |String| Month and year for next year's publication, in "Month YYYY" format |
| sixMonthsAgo   |String| Month and year for publication from 6 months ago, in "Month YYYY" format |
| twelveMonthsAgo|String| Month and year for publication from 12 months ago, in "Month YYYY" format |
| twoMonthsAgo   |String| Month and year for publication from 2 months ago, in "Month YYYY" format |
| displayWeek     |String|Month and day indicating week to display the current edition, in "Month DD" format|
| edition        |String| Publication date in "Month DD, YYYY" format |



#### Example JSON Response

```
{
  "href": "https://integration1.api.manheim.com/valuations/edition",
  "count": 1,
  "items": [
    {
      "date": "2017-01-25",
      "monthAndDay": "Jan 20",
      "nextMonth": "Feb 2017",
      "nextYear": "Jan 2018",
      "sixMonthsAgo": "Jul 2016",
      "twelveMonthsAgo": "Jan 2016",
      "twoMonthsAgo": "Nov 2016",
      "displayWeek": "Feb 01",
      "edition": "January 25, 2017"
    }
  ]
}
```







<a name="retrieveAllRegions"></a>

### Retrieve All Regions

#### Endpoint

```
GET https://integration1.api.manheim.com/valuations/regions
```


#### Description 

This method allows an API user to retrieve all of the regions that may be used as a query parameter to obtain region-adjusted valuations. See ["Retrieve Valuations by VIN"](/#/apis/marketplace/valuations#retrieveValuationsByVIN  "Valuations API") for more information.



#### Common Return Codes

|Response Code | Response Message | Possible Next Actions |
|--------------|------------------|-----------------------|
|200 OK        |Body contains the requested information | Successful response; no actions necessary |
|401 Unauthorized | **ERROR:** Developer inactive | API token may be malformed or the user does not have access; check the token or contact Manheim for further support |
|404 Not Found    | **ERROR:** HTML response may contain details about the error | URL may be malformed; check and resubmit | 
|500 Server Error | **ERROR:** Unknown Error | Resubmit the request; if issue still exists contact Manheim for support |



#### Request Parameters 

This method only allows the following OPTIONAL query string parameters. 

| Parameter | Type | Description |
|-----------|-------|------------|
| country   | String| API calls will default to US if this parameter is omitted; accepted values: US for United States, CA for CANADA |


#### Example JSON Request

The URL may include an optional query string to retrieve Canadian regions, as shown in the following example. 

```
GET https://integration1.api.manheim.com/valuations/regions?country=CA
```


<a name="regionResponse"></a>



#### Response Parameters


The overall JSON object for region information has the following fields.

|Field | Type  | Description |
|------|-------|------------|
|href  |String | URL of the request |
|count |Integer| Number of regions returned |
|**items** | Array | A block containing information about one or more regions; each item of region information has the fields listed in the table below, and the number of regions matches the value of the "count" field |

Each region item within the JSON object has the following fields.

| Field   | Type     | Description | 
| --------|--------- | ----- |
| href    |String | URL containing information about a specific region | 
| id      | String |Region ID |
| name    | String |Full region name |


#### Example JSON Response

The response for regions of the United States is similar to the following. 
```
{
  "href": "https://integration1.api.manheim.com/valuations/regions",
  "count": 6,
  "items": [
    {
      "href": "https://integration1.api.manheim.com/valuations/regions/id/NA?country=US",
      "id": "NA",
      "name": "National"
    },
    {
      "href": "https://integration1.api.manheim.com/valuations/regions/id/SE?country=US",
      "id": "SE",
      "name": "Southeast"
    },
    {
      "href": "https://integration1.api.manheim.com/valuations/regions/id/NE?country=US",
      "id": "NE",
      "name": "Northeast"
    },
    {
      "href": "https://integration1.api.manheim.com/valuations/regions/id/MW?country=US",
      "id": "MW",
      "name": "Midwest"
    },
    {
      "href": "https://integration1.api.manheim.com/valuations/regions/id/SW?country=US",
      "id": "SW",
      "name": "Southwest"
    },
    {
      "href": "https://integration1.api.manheim.com/valuations/regions/id/WC?country=US",
      "id": "WC",
      "name": "West Coast"
    }
  ]
}
```

The response for the Canadian regions is similar to the following. 

```
{
  "href": "https://integration1.api.manheim.com/valuations/regions?country=CA",
  "count": 5,
  "items": [
    {
      "href": "https://integration1.api.manheim.com/valuations/regions/id/NA?country=CA",
      "id": "NA",
      "name": "National"
    },
    {
      "href": "https://integration1.api.manheim.com/valuations/regions/id/ON?country=CA",
      "id": "ON",
      "name": "Ontario"
    },
    {
      "href": "https://integration1.api.manheim.com/valuations/regions/id/QU?country=CA",
      "id": "QU",
      "name": "Quebec"
    },
    {
      "href": "https://integration1.api.manheim.com/valuations/regions/id/AT?country=CA",
      "id": "AT",
      "name": "Atlantic"
    },
    {
      "href": "https://integration1.api.manheim.com/valuations/regions/id/WE?country=CA",
      "id": "WE",
      "name": "Western"
    }
  ]
}
```



### Retrieve a Single Region 

#### Endpoint 

```
GET https://integration1.api.manheim.com/valuations/regions/id/ID
```


#### Description 

This method allows a user to retrieve information about a specific region. 

#### Common Return Codes

|Response Code | Response Message | Possible Next Actions |
|--------------|------------------|---------------------|
|200 OK        |Body contains the requested information | Successful response; no actions necessary |
|401 Unauthorized | **ERROR:** Developer inactive | API token may be malformed or the user does not have access; check the token or contact Manheim for further support |
|404 Not Found    | **ERROR:** HTML response may contain details about the error | URL may be malformed; check and resubmit |
|500 Server Error | **ERROR:** Unknown Error | Resubmit the request; if issue still exists contact Manheim for support |



 
#### Request Parameters 

This method only allows the following OPTIONAL query string parameters. 

| Parameter | Type | Description |
|-----------|-------|------------|
| country   | String| API calls will default to US if this parameter is omitted; accepted values: US for United States, CA for CANADA |



#### Example JSON Request

The following shows an example of the request using a query string parameter. Note that if the auction is in Canada, the request must include the *country* parameter with the value *CA*.

```
GET https://integration1.api.manheim.com/valuations/regions/id/ON?country=CA
```


#### Response Parameters

This method has the same fields in the response as the method to ["Retrieve All Regions"](/#/apis/marketplace/valuations#regionResponse "Region Response Fields"). 


#### Example JSON Response

```
{
  "href": "https://integration1.api.manheim.com/valuations/regions/id/SE?country=US",
  "count": 1,
  "items": [
    {
      "href": "https://integration1.api.manheim.com/valuations/regions/id/SE?country=US",
      "id": "SE",
      "name": "Southeast"
    }
  ]
}
```


### Retrieve Region by Auction 

#### Endpoint

```
GET https://integration1.api.manheim.com/valuations/regions/auction/id/ID
```


#### Description 

This method allows the user search for the region in which an auction is located. 

#### Common Return Codes

|Response Code | Response Message | Possible Next Actions |
|--------------|------------------|---------------------|
|200 OK        |Body contains the requested information | Successful response; no actions necessary |
|401 Unauthorized | **ERROR:** Developer inactive | API token may be malformed or the user does not have access; check the token or contact Manheim for further support | 
|404 Not Found    | **ERROR:** HTML response may contain details about the error | URL may be malformed; check and resubmit |
|500 Server Error | **ERROR:** Unknown Error | Resubmit the request; if issue still exists contact Manheim for support |



#### Request Parameters 

This method required the auction ID in the URL request. 

The following OPTIONAL query string parameters may be included in the URL. 

| Parameter | Type | Description |
|-----------|-------|------------|
| country   | String| Identifies the country in which the region is located; accepted values are US for United States, CA for CANADA. API calls will default to US if this parameter is omitted  |



#### Example JSON Request

"ID" at the end of the URL should be replaced with the auction ID assigned by Manheim, as shown in the example below.

```
GET https://integration1.api.manheim.com/valuations/regions/auction/id/AAA
```


#### Response Parameters

This method has the same fields in the response as the method to ["Retrieve All Regions"](/#/apis/marketplace/valuations#regionResponse "Region Response Fields"). 

#### Example JSON Response

```
{
  "href": "https://integration1.api.manheim.com/valuations/regions/auction/id/AAA",
  "count": 1,
  "items": [
    {
      "href": "https://integration1.api.manheim.com/valuations/regions/auction/id/AAA?country=US",
      "id": "SE",
      "name": "Southeast"
    }
  ]
}
```


The following example shows a response to a request specifying an auction in Canada.

```
{
	"href": "https://integration1.api.manheim.com/valuations/regions/auction/id/HLFX?country=CA",
	"count": 1,
	"items": [
	  {
		"href": "https://integration1.api.manheim.com/valuations/regions/auction/id/HLFX?country=CA",
		"id": "AT",
		"name": "Atlantic"
	  }
  ]
}
```




<a name="retrieveBatchValuationsByMID"></a>


### Retrieve Batch Valuations by MID 

#### Endpoint 

```
POST https://integration1.api.manheim.com/valuations/batch/ids
```


#### Description 

This method allows the user to retrieve valuations for up to 500 MIDs per request.

#### Common Return Codes

|Response Code | Response Message | Possible Next Actions |
|-----|-----|-----|
|200 OK | Body containsponse contains the requested information | Successful response; no actions necessary |
|400 Bad Request | **ERROR:** Message contains details about the error | MIDs may be malformed or missing or the URL may be malformed; check and resubmit | 
|401 Unauthorized | **ERROR:** Developer inactive | API token may be malformed or the user does not have access; check the token or contact Manheim for further support |
|500 Server Error | **ERROR:** Unknown Error | Resubmit the request; if issue still exists contact Manheim for support |



<a name="midRequest"></a>


#### Request Parameters 


The body of this request uses MIDs to retrieve valuations. 

|Parameter |Type | Requirement | Description |
|----------|-----|-------------|--------------|
|ids       |String |REQUIRED | each individual request in the POST body must include the MID for the vehicle; this can be followed by any optional parameters |


The following OPTIONAL query string parameters are available for this method. 

| Parameter | Type | Description |
|-----------|-------|------------|
| country   | String| API calls will default to US if this parameter is omitted; accepted values: US for United States, CA for CANADA |
| odometer  |Integer| Accepts numeric values but currently matches only exact values rather than a range of values |
| region    |String |API calls will default to NA if this parameter is omitted; accepted values can be retrieved by the API call, Retrieve All Regions |
|color |String | External color of the vehicle; accepted values may be retrieved from the request "Retrieve All Colors" |
|grade |Integer| Condition grade of the vehicle such that "30" is equivalent to "3.0" |
| orgId     |String | Characters that identify the individual or organization requesting the valuation. Coordinate with your Manheim account representative to set up orgId's. |
| zipCode   |String | Location of the vehicle as a 5-digit postal code, e.g. "30019. |
| geoLocation  |String | Location of the vehicle in the form of a latitude and longitude, as in '33.9335,-84.3958' |
| include   |String | Accepts any comma-separated combination of the following, in any order: retail, forecast, historical |




#### Example JSON Request

```
POST https://integration1.api.manheim.com/valuations/batch/ids
```

The POST body for the batch request may contain partial URLs for multiple MIDs. Full URLs are not permitted and will cause an error to occur. Each URL may be entered on a separate line for readability.


```
[
   "201308559801684?country=CA",
   "200702319231492?region=NE",
   "200900612001137?odometer=5000"
]
```



The request may contain additional query string parameters, as shown in the following example. 

```
[
   "201308559801684?odometer=55000&region=mw",
   "201505807831389?odometer=37000&region=ne&color=silver",
   "201705807831389?odometer=14000&region=se&color=red&grade=40"
]
```


This example shows a JSON request for multiple valuations, one of which uses the "include" parameter to obtain retail, historical, and forecast information. The response for this request is shown in the Example JSON Response section. 


```
[
	"201300625416689?odometer=37000&region=mw&include=retail,historical,forecast",
	"201300625416690?odometer=37000&region=ne&color=white",
	"200900600178267?odometer=21000&region=se&color=silver&grade=36"
]
```




#### Response Parameters

The batch call has the fields listed below. The fields for each valuation item may be found in the method to ["Retrieve Valuations by VIN"](/#/apis/marketplace/valuations#responseFields "Valuation Response Fields"). 


|Field             | Notes |
|------------------|-------|
|href              |URL of the request |
|**items**         |Contains an array of information about the batch request |
|items.count       |Number of successful valuations found for the request |
|items.items       |Contains an array of individual valuations |
|**errors**        |Contains an array of error information if any are found |
|errors.count      |Number of errors found for a batch request |
|**errors.errors** |Contains an array of information about each individual error found within a batch request |

Each error within the batch call has the following fields.

|Field            | Notes |
|-----------------|-------|
|href             |URL of the individual valuation request within the batch request that caused the error |
|message          |Details about the error |
|developerMessage |Error code, such as "Invalid ID" |



#### Example JSON Response

```
{
    "href": "https://integration1.api.manheim.com/valuations/batch/vins",
    "items": [
        {
            "count": 3,
            "items": [
                {
                    "href": "https://integration1.api.manheim.com/valuations/vin/5J6RE4H76AL093425?country=CA&include=retail,historical,forecast",
                    "count": 1,
                    "items": [
                        {
                            "href": "https://integration1.api.manheim.com/valuations/id/201002319980048?country=CA&include=retail,historical,forecast",
                            "description": {
                                "year": 2010,
                                "make": "HONDA",
                                "model": "CR-V 4WD",
                                "trim": "4D SUV EX-L",
                                "subSeries": "EX-L"
                            },
                            "adjustedPricing": {
                                "wholesale": {
                                    "above": 9900,
                                    "average": 9250,
                                    "below": 8600
                                },
                                "retail": {
                                    "above": 11200,
                                    "average": 10500,
                                    "below": 9800
                                },
                                "adjustedBy": {}
                            },
                            "wholesale": {
                                "above": 9900,
                                "average": 9250,
                                "below": 8600
                            },
                            "retail": {
                                "above": 11200,
                                "average": 10500,
                                "below": 9800
                            },
                            "historicalAverages": {
                                "last30Days": {
                                    "odometer": 186378,
                                    "price": 8300
                                },
                                "lastMonth": {
                                    "odometer": 0,
                                    "price": 0
                                },
                                "lastTwoMonths": {
                                    "odometer": 0,
                                    "price": 0
                                },
                                "lastSixMonths": {
                                    "odometer": 176141,
                                    "price": 9550
                                },
                                "lastYear": {
                                    "odometer": 0,
                                    "price": 0
                                }
                            },
                            "forecast": {
                                "nextMonth": {
                                    "wholesale": 9250,
                                    "retail": 10500
                                },
                                "nextYear": {
                                    "wholesale": 8900,
                                    "retail": 10100
                                }
                            },
                            "averageOdometer": 167135,
                            "odometerUnits": "kilometers",
                            "averageGrade": 33,
                            "currency": "CAD",
                            "bestMatch": true,
                            "samples": {
                                "href": "https://integration1.api.manheim.com/valuation-samples/id/201002319980048?country=CA&orderBy=location%20desc&start=1&limit=25"
                            }
                        }
                    ]
                },
                {
                    "href": "https://integration1.api.manheim.com/valuations/vin/3GTU2UEC5EG453829?country=US&region=NE&color=white",
                    "count": 1,
                    "items": [
                        {
                            "href": "https://integration1.api.manheim.com/valuations/id/201402159150218?country=US&region=NE&color=WHITE",
                            "description": {
                                "year": 2014,
                                "make": "GMC",
                                "model": "1500 SIERRA 4WD V8 FFV",
                                "trim": "CREW CAB 5.3L SLE",
                                "subSeries": "SLE"
                            },
                            "adjustedPricing": {
                                "wholesale": {
                                    "above": 27000,
                                    "average": 23600,
                                    "below": 20100
                                },
                                "adjustedBy": {
                                    "Color": "WHITE",
                                    "ColorAdjustmentValue": {
                                        "wholesale": {
                                            "above": 40,
                                            "average": 40,
                                            "below": 30
                                        }
                                    },
                                    "Region": "NE",
                                    "RegionAdjustmentValue": {
                                        "wholesale": {
                                            "above": -50,
                                            "average": -40,
                                            "below": -40
                                        }
                                    }
                                }
                            },
                            "wholesale": {
                                "above": 27000,
                                "average": 23600,
                                "below": 20100
                            },
                            "averageOdometer": 75190,
                            "odometerUnits": "miles",
                            "averageGrade": 38,
                            "currency": "USD",
                            "bestMatch": true,
                            "samples": {
                                "href": "https://integration1.api.manheim.com/valuation-samples/id/201402159150218?country=US&orderBy=location%20desc&start=1&limit=25"
                            }
                        }
                    ]
                },
                {
                    "href": "https://integration1.api.manheim.com/valuations/vin/1FMCU9HXXDUC55952?country=US&odometer=5000&grade=36",
                    "count": 1,
                    "items": [
                        {
                            "href": "https://integration1.api.manheim.com/valuations/id/201301766060786?country=US&odometer=5000&grade=36",
                            "description": {
                                "year": 2013,
                                "make": "FORD",
                                "model": "ESCAPE 4WD",
                                "trim": "4D SUV 1.6L SEL",
                                "subSeries": "SEL"
                            },
                            "adjustedPricing": {
                                "wholesale": {
                                    "above": 11250,
                                    "average": 9775,
                                    "below": 8275
                                },
                                "adjustedBy": {
                                    "Grade": "36",
                                    "GradeAdjustmentValue": {
                                        "wholesale": {
                                            "above": -3750,
                                            "average": -3250,
                                            "below": -2750
                                        }
                                    },
                                    "Odometer": "5000",
                                    "OdometerAdjustmentValue": "4000"
                                }
                            },
                            "wholesale": {
                                "above": 11050,
                                "average": 9025,
                                "below": 7025
                            },
                            "averageOdometer": 91727,
                            "odometerUnits": "miles",
                            "averageGrade": 34,
                            "currency": "USD",
                            "bestMatch": true,
                            "samples": {
                                "href": "https://integration1.api.manheim.com/valuation-samples/id/201301766060786?country=US&orderBy=location%20desc&start=1&limit=25"
                            }
                        }
                    ]
                }
            ]
        }
    ],
    "errors": [
        {
            "count": 0,
            "errors": []
        }
    ]
}
```



<a name="batchByMid-ResponseWith-include-color-grade"></a>


This example includes responses for the parameters "include", "color", and "grade". 

```
{
    "href": "https://integration1.api.manheim.com/valuations/batch/ids",
    "items": [
        {
            "count": 3,
            "items": [
                {
                    "href": "https://integration1.api.manheim.com/valuations/id/201300625416689?country=US&odometer=37000&region=MW&include=retail,historical,forecast",
                    "description": {
                        "year": 2013,
                        "make": "B M W",
                        "model": "X SERIES",
                        "trim": "X3 4D SUV 2.0L 28I XDRIVE",
                        "subSeries": "28I XDRIVE"
                    },
                    "adjustedPricing": {
                        "wholesale": {
                            "above": 18600,
                            "average": 16050,
                            "below": 13500
                        },
                        "retail": {
                            "above": 24200,
                            "average": 20700,
                            "below": 17300
                        },
                        "adjustedBy": {
                            "Odometer": "37000",
                            "OdometerAdjustmentValue": "4220",
                            "Region": "MW",
                            "RegionAdjustmentValue": {
                                "wholesale": {
                                    "above": 30,
                                    "average": 20,
                                    "below": 20
                                },
                                "retail": {
                                    "above": 40,
                                    "average": 30,
                                    "below": 30
                                }
                            }
                        }
                    },
                    "wholesale": {
                        "above": 14400,
                        "average": 11800,
                        "below": 9250
                    },
                    "retail": {
                        "above": 19900,
                        "average": 16500,
                        "below": 13050
                    },
                    "historicalAverages": {
                        "last30Days": {
                            "odometer": 78727,
                            "price": 12000
                        },
                        "lastMonth": {
                            "odometer": 82014,
                            "price": 11750
                        },
                        "lastTwoMonths": {
                            "odometer": 77391,
                            "price": 12350
                        },
                        "lastSixMonths": {
                            "odometer": 69946,
                            "price": 13800
                        },
                        "lastYear": {
                            "odometer": 68595,
                            "price": 14850
                        }
                    },
                    "forecast": {
                        "nextMonth": {
                            "wholesale": 11650,
                            "retail": 16250
                        },
                        "nextYear": {
                            "wholesale": 8750,
                            "retail": 12350
                        }
                    },
                    "averageOdometer": 80329,
                    "odometerUnits": "miles",
                    "averageGrade": 37,
                    "currency": "USD",
                    "samples": {
                        "href": "https://integration1.api.manheim.com/valuation-samples/id/201300625416689?country=US&orderBy=location%20desc&start=1&limit=25"
                    }
                },
                {
                    "href": "https://integration1.api.manheim.com/valuations/id/201300625416690?country=US&odometer=37000&region=NE&color=WHITE",
                    "description": {
                        "year": 2013,
                        "make": "B M W",
                        "model": "X SERIES",
                        "trim": "X3 4D SUV 3.0L 35I XDRIVE",
                        "subSeries": "35I XDRIVE"
                    },
                    "adjustedPricing": {
                        "wholesale": {
                            "above": 21200,
                            "average": 18950,
                            "below": 16700
                        },
                        "adjustedBy": {
                            "Color": "WHITE",
                            "ColorAdjustmentValue": {
                                "wholesale": {
                                    "above": 300,
                                    "average": 270,
                                    "below": 240
                                }
                            },
                            "Odometer": "37000",
                            "OdometerAdjustmentValue": "3170",
                            "Region": "NE",
                            "RegionAdjustmentValue": {
                                "wholesale": {
                                    "above": 190,
                                    "average": 170,
                                    "below": 150
                                }
                            }
                        }
                    },
                    "wholesale": {
                        "above": 17550,
                        "average": 15350,
                        "below": 13150
                    },
                    "averageOdometer": 70422,
                    "odometerUnits": "miles",
                    "averageGrade": 36,
                    "currency": "USD",
                    "samples": {
                        "href": "https://integration1.api.manheim.com/valuation-samples/id/201300625416690?country=US&orderBy=location%20desc&start=1&limit=25"
                    }
                },
                {
                    "href": "https://integration1.api.manheim.com/valuations/id/200900600178267?country=US&odometer=21000&region=SE&color=SILVER&grade=36",
                    "description": {
                        "year": 2009,
                        "make": "B M W",
                        "model": "3 SERIES",
                        "trim": "328XI 4D SEDAN"
                    },
                    "adjustedPricing": {
                        "wholesale": {
                            "above": 7700,
                            "average": 6550,
                            "below": 5425
                        },
                        "adjustedBy": {
                            "Color": "SILVER",
                            "ColorAdjustmentValue": {
                                "wholesale": {
                                    "above": -120,
                                    "average": -100,
                                    "below": -80
                                }
                            },
                            "Grade": "36",
                            "GradeAdjustmentValue": {
                                "wholesale": {
                                    "above": -2600,
                                    "average": -2210,
                                    "below": -1830
                                }
                            },
                            "Odometer": "21000",
                            "OdometerAdjustmentValue": "3100",
                            "Region": "SE",
                            "RegionAdjustmentValue": {
                                "wholesale": {
                                    "above": 10,
                                    "average": 0,
                                    "below": 0
                                }
                            }
                        }
                    },
                    "wholesale": {
                        "above": 7350,
                        "average": 5800,
                        "below": 4250
                    },
                    "averageOdometer": 98600,
                    "odometerUnits": "miles",
                    "averageGrade": 31,
                    "currency": "USD",
                    "samples": {
                        "href": "https://integration1.api.manheim.com/valuation-samples/id/200900600178267?country=US&orderBy=location%20desc&start=1&limit=25"
                    }
                }
            ]
        }
    ],
    "errors": [
        {
            "count": 0,
            "errors": []
        }
    ]
}
```


</private>




<a name="retrieveBatchValuationsByVIN"></a>


### Retrieve Batch Valuations by VIN 

#### Endpoint 

```
POST https://integration1.api.manheim.com/valuations/batch/vins
```


#### Description 

This method allows a user to retrieve up to 100 valuations using VINs in a single request.

#### Common Return Codes

|Response Code | Response Message | Possible Next Actions |
|-----|-----|-----|
|200 OK | Body contains the requested valuation(s) | Successful response; no actions necessary |
|400 Bad Request | **ERROR:** Message contains details about the error | VINs may be malformed or missing or the URL may be malformed; check and resubmit | 
|401 Unauthorized | **ERROR:** Developer inactive | API token may be malformed or the user does not have access; check the token or contact Manheim for further support | 
|500 Server Error | **ERROR:** Unknown Error | Resubmit the request; if issue still exists contact Manheim for support |




#### Request Parameters 

The body of this request uses VINs to retrieve valuations. 

|Parameter |Type | Requirement | Description |
|----------|-----|-------------|--------------|
|VIN          |String |REQUIRED | vehicle identification number (VIN) of a vehicle |


Requests may also include the optional parameters described for the method ["Retrieve Batch Valuations by MID"](/#/apis/marketplace/valuations#midRequest "Batch Parameters").




#### Example JSON Request

```
POST https://integration1.api.manheim.com/valuations/batch/vins
```

The POST body for the batch request may contain partial URLs for multiple VINs. Full URLs are not permitted and will cause an error to occur. Each URL may be entered on a separate line for readability.


```
[
	"3VWD07AJ5EM292070?country=CA",
	"3GTU2UEC5EG453829?region=NE",
	"1FMCU9HXXDUC55952?odometer=5000"
]
```



This example shows a JSON request body for retrieving multiple valuations using optional query parameters for the country; historical, retail, and projected pricing; region, color, and grade. The matching response is shown in the Example JSON Response section.

```
[
	"5J6RE4H76AL093425?country=CA&include=historical,retail,forecast",
	"3GTU2UEC5EG453829?region=NE&color=white",
	"1FMCU9HXXDUC55952?odometer=5000&grade=36"
]
```





#### Response Parameters

This method returns the same fields as the method to ["Retrieve Batch Valuations by MID"](/#/apis/marketplace/valuations#batchMid "Response to a Batch Request").


#### Example JSON Response

This example show a response to a batch request specifying a different combination of parameters for each individual request



```
{
    "href": "https://integration1.api.manheim.com/valuations/batch/vins",
    "items": [
        {
            "count": 3,
            "items": [
                {
                    "href": "https://integration1.api.manheim.com/valuations/vin/5J6RE4H76AL093425?country=CA&include=retail,historical,forecast",
                    "count": 1,
                    "items": [
                        {
                            "href": "https://integration1.api.manheim.com/valuations/id/201002319980048?country=CA&include=retail,historical,forecast",
                            "description": {
                                "year": 2010,
                                "make": "HONDA",
                                "model": "CR-V 4WD",
                                "trim": "4D SUV EX-L",
                                "subSeries": "EX-L"
                            },
                            "adjustedPricing": {
                                "wholesale": {
                                    "above": 9900,
                                    "average": 9250,
                                    "below": 8600
                                },
                                "retail": {
                                    "above": 11200,
                                    "average": 10500,
                                    "below": 9800
                                },
                                "adjustedBy": {}
                            },
                            "wholesale": {
                                "above": 9900,
                                "average": 9250,
                                "below": 8600
                            },
                            "retail": {
                                "above": 11200,
                                "average": 10500,
                                "below": 9800
                            },
                            "historicalAverages": {
                                "last30Days": {
                                    "odometer": 186378,
                                    "price": 8300
                                },
                                "lastMonth": {
                                    "odometer": 0,
                                    "price": 0
                                },
                                "lastTwoMonths": {
                                    "odometer": 0,
                                    "price": 0
                                },
                                "lastSixMonths": {
                                    "odometer": 176141,
                                    "price": 9550
                                },
                                "lastYear": {
                                    "odometer": 0,
                                    "price": 0
                                }
                            },
                            "forecast": {
                                "nextMonth": {
                                    "wholesale": 9250,
                                    "retail": 10500
                                },
                                "nextYear": {
                                    "wholesale": 8900,
                                    "retail": 10100
                                }
                            },
                            "averageOdometer": 167135,
                            "odometerUnits": "kilometers",
                            "averageGrade": 33,
                            "currency": "CAD",
                            "bestMatch": true,
                            "samples": {
                                "href": "https://integration1.api.manheim.com/valuation-samples/id/201002319980048?country=CA&orderBy=location%20desc&start=1&limit=25"
                            }
                        }
                    ]
                },
                {
                    "href": "https://integration1.api.manheim.com/valuations/vin/3GTU2UEC5EG453829?country=US&region=NE&color=white",
                    "count": 1,
                    "items": [
                        {
                            "href": "https://integration1.api.manheim.com/valuations/id/201402159150218?country=US&region=NE&color=WHITE",
                            "description": {
                                "year": 2014,
                                "make": "GMC",
                                "model": "1500 SIERRA 4WD V8 FFV",
                                "trim": "CREW CAB 5.3L SLE",
                                "subSeries": "SLE"
                            },
                            "adjustedPricing": {
                                "wholesale": {
                                    "above": 27000,
                                    "average": 23600,
                                    "below": 20100
                                },
                                "adjustedBy": {
                                    "Color": "WHITE",
                                    "ColorAdjustmentValue": {
                                        "wholesale": {
                                            "above": 40,
                                            "average": 40,
                                            "below": 30
                                        }
                                    },
                                    "Region": "NE",
                                    "RegionAdjustmentValue": {
                                        "wholesale": {
                                            "above": -50,
                                            "average": -40,
                                            "below": -40
                                        }
                                    }
                                }
                            },
                            "wholesale": {
                                "above": 27000,
                                "average": 23600,
                                "below": 20100
                            },
                            "averageOdometer": 75190,
                            "odometerUnits": "miles",
                            "averageGrade": 38,
                            "currency": "USD",
                            "bestMatch": true,
                            "samples": {
                                "href": "https://integration1.api.manheim.com/valuation-samples/id/201402159150218?country=US&orderBy=location%20desc&start=1&limit=25"
                            }
                        }
                    ]
                },
                {
                    "href": "https://integration1.api.manheim.com/valuations/vin/1FMCU9HXXDUC55952?country=US&odometer=5000&grade=36",
                    "count": 1,
                    "items": [
                        {
                            "href": "https://integration1.api.manheim.com/valuations/id/201301766060786?country=US&odometer=5000&grade=36",
                            "description": {
                                "year": 2013,
                                "make": "FORD",
                                "model": "ESCAPE 4WD",
                                "trim": "4D SUV 1.6L SEL",
                                "subSeries": "SEL"
                            },
                            "adjustedPricing": {
                                "wholesale": {
                                    "above": 11250,
                                    "average": 9775,
                                    "below": 8275
                                },
                                "adjustedBy": {
                                    "Grade": "36",
                                    "GradeAdjustmentValue": {
                                        "wholesale": {
                                            "above": -3750,
                                            "average": -3250,
                                            "below": -2750
                                        }
                                    },
                                    "Odometer": "5000",
                                    "OdometerAdjustmentValue": "4000"
                                }
                            },
                            "wholesale": {
                                "above": 11050,
                                "average": 9025,
                                "below": 7025
                            },
                            "averageOdometer": 91727,
                            "odometerUnits": "miles",
                            "averageGrade": 34,
                            "currency": "USD",
                            "bestMatch": true,
                            "samples": {
                                "href": "https://integration1.api.manheim.com/valuation-samples/id/201301766060786?country=US&orderBy=location%20desc&start=1&limit=25"
                            }
                        }
                    ]
                }
            ]
        }
    ],
    "errors": [
        {
            "count": 0,
            "errors": []
        }
    ]
}
```









