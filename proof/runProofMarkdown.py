#Proof and Edit a Markdown File in Developer Portal repo

import proofMarkdown

targetFile = '../test-targets/valuations.md'

reportFile = '../output-reports/report.txt'

uniqueIdFields = ['auctionId', 'customerId', 'accountId', 'manheimAccountNumber', 'workOrderNumber', 'sellerNumber', 'sblu', 'dealerNumber', 'dealerName', 'addressLine', 'addressCity', 'addressState', 'addressZip', 'contactNumber', 'groupCode', 'dealerGroupCode', 'locationCode', 'consignorCode', 'offeringGroupCode', 'otherRegistrationUserId', 'registrationUserId', 'signerName', 'auctionInitials', 'auctioneerInitials', 'buyerNumber', 'operatorNumber', 'saleYear', 'saleNumber', 'laneNumber', 'runNumber', 'saleDate', 'repNumber', 'oveListingId', 'number', 'phone', 'email', 'vin', 'auth_tkt']



proofMarkdown.writeHeader(targetFile, reportFile)

proofMarkdown.findDuplicateRowsInTables(targetFile, reportFile)

proofMarkdown.identifyUniqueIds(targetFile, uniqueIdFields, reportFile)

proofMarkdown.identifyRequestExamples(targetFile, reportFile)

proofMarkdown.findHrefsInJsonSamples(targetFile, reportFile)

#proofAndEditMarkdown.spellcheckFile(targetFile, 'google-10000-english.txt', reportFile)
proofMarkdown.spellcheckFile(targetFile, '../reference/words_alpha.txt', '../reference/specializedWords.txt', reportFile)


