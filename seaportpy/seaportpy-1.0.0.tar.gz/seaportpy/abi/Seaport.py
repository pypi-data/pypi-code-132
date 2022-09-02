SEAPORT_ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "conduitController", "type": "address"}
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {"inputs": [], "name": "BadContractSignature", "type": "error"},
    {"inputs": [], "name": "BadFraction", "type": "error"},
    {
        "inputs": [
            {"internalType": "address", "name": "token", "type": "address"},
            {"internalType": "address", "name": "from", "type": "address"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "BadReturnValueFromERC20OnTransfer",
        "type": "error",
    },
    {
        "inputs": [{"internalType": "uint8", "name": "v", "type": "uint8"}],
        "name": "BadSignatureV",
        "type": "error",
    },
    {"inputs": [], "name": "ConsiderationCriteriaResolverOutOfRange", "type": "error"},
    {
        "inputs": [
            {"internalType": "uint256", "name": "orderIndex", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "considerationIndex",
                "type": "uint256",
            },
            {"internalType": "uint256", "name": "shortfallAmount", "type": "uint256"},
        ],
        "name": "ConsiderationNotMet",
        "type": "error",
    },
    {"inputs": [], "name": "CriteriaNotEnabledForItem", "type": "error"},
    {
        "inputs": [
            {"internalType": "address", "name": "token", "type": "address"},
            {"internalType": "address", "name": "from", "type": "address"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256[]", "name": "identifiers", "type": "uint256[]"},
            {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"},
        ],
        "name": "ERC1155BatchTransferGenericFailure",
        "type": "error",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "account", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "EtherTransferGenericFailure",
        "type": "error",
    },
    {"inputs": [], "name": "InexactFraction", "type": "error"},
    {"inputs": [], "name": "InsufficientEtherSupplied", "type": "error"},
    {"inputs": [], "name": "InvalidBasicOrderParameterEncoding", "type": "error"},
    {
        "inputs": [{"internalType": "address", "name": "conduit", "type": "address"}],
        "name": "InvalidCallToConduit",
        "type": "error",
    },
    {"inputs": [], "name": "InvalidCanceller", "type": "error"},
    {
        "inputs": [
            {"internalType": "bytes32", "name": "conduitKey", "type": "bytes32"},
            {"internalType": "address", "name": "conduit", "type": "address"},
        ],
        "name": "InvalidConduit",
        "type": "error",
    },
    {"inputs": [], "name": "InvalidERC721TransferAmount", "type": "error"},
    {"inputs": [], "name": "InvalidFulfillmentComponentData", "type": "error"},
    {
        "inputs": [{"internalType": "uint256", "name": "value", "type": "uint256"}],
        "name": "InvalidMsgValue",
        "type": "error",
    },
    {"inputs": [], "name": "InvalidProof", "type": "error"},
    {
        "inputs": [{"internalType": "bytes32", "name": "orderHash", "type": "bytes32"}],
        "name": "InvalidRestrictedOrder",
        "type": "error",
    },
    {"inputs": [], "name": "InvalidSignature", "type": "error"},
    {"inputs": [], "name": "InvalidSigner", "type": "error"},
    {"inputs": [], "name": "InvalidTime", "type": "error"},
    {
        "inputs": [],
        "name": "MismatchedFulfillmentOfferAndConsiderationComponents",
        "type": "error",
    },
    {
        "inputs": [{"internalType": "enum Side", "name": "side", "type": "uint8"}],
        "name": "MissingFulfillmentComponentOnAggregation",
        "type": "error",
    },
    {"inputs": [], "name": "MissingItemAmount", "type": "error"},
    {"inputs": [], "name": "MissingOriginalConsiderationItems", "type": "error"},
    {
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "NoContract",
        "type": "error",
    },
    {"inputs": [], "name": "NoReentrantCalls", "type": "error"},
    {"inputs": [], "name": "NoSpecifiedOrdersAvailable", "type": "error"},
    {
        "inputs": [],
        "name": "OfferAndConsiderationRequiredOnFulfillment",
        "type": "error",
    },
    {"inputs": [], "name": "OfferCriteriaResolverOutOfRange", "type": "error"},
    {
        "inputs": [{"internalType": "bytes32", "name": "orderHash", "type": "bytes32"}],
        "name": "OrderAlreadyFilled",
        "type": "error",
    },
    {"inputs": [], "name": "OrderCriteriaResolverOutOfRange", "type": "error"},
    {
        "inputs": [{"internalType": "bytes32", "name": "orderHash", "type": "bytes32"}],
        "name": "OrderIsCancelled",
        "type": "error",
    },
    {
        "inputs": [{"internalType": "bytes32", "name": "orderHash", "type": "bytes32"}],
        "name": "OrderPartiallyFilled",
        "type": "error",
    },
    {"inputs": [], "name": "PartialFillsNotEnabledForOrder", "type": "error"},
    {
        "inputs": [
            {"internalType": "address", "name": "token", "type": "address"},
            {"internalType": "address", "name": "from", "type": "address"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "identifier", "type": "uint256"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"},
        ],
        "name": "TokenTransferGenericFailure",
        "type": "error",
    },
    {"inputs": [], "name": "UnresolvedConsiderationCriteria", "type": "error"},
    {"inputs": [], "name": "UnresolvedOfferCriteria", "type": "error"},
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "newCounter",
                "type": "uint256",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "offerer",
                "type": "address",
            },
        ],
        "name": "CounterIncremented",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "bytes32",
                "name": "orderHash",
                "type": "bytes32",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "offerer",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "zone",
                "type": "address",
            },
        ],
        "name": "OrderCancelled",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "bytes32",
                "name": "orderHash",
                "type": "bytes32",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "offerer",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "zone",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "recipient",
                "type": "address",
            },
            {
                "components": [
                    {
                        "internalType": "enum ItemType",
                        "name": "itemType",
                        "type": "uint8",
                    },
                    {"internalType": "address", "name": "token", "type": "address"},
                    {
                        "internalType": "uint256",
                        "name": "identifier",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "amount", "type": "uint256"},
                ],
                "indexed": False,
                "internalType": "struct SpentItem[]",
                "name": "offer",
                "type": "tuple[]",
            },
            {
                "components": [
                    {
                        "internalType": "enum ItemType",
                        "name": "itemType",
                        "type": "uint8",
                    },
                    {"internalType": "address", "name": "token", "type": "address"},
                    {
                        "internalType": "uint256",
                        "name": "identifier",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "amount", "type": "uint256"},
                    {
                        "internalType": "address payable",
                        "name": "recipient",
                        "type": "address",
                    },
                ],
                "indexed": False,
                "internalType": "struct ReceivedItem[]",
                "name": "consideration",
                "type": "tuple[]",
            },
        ],
        "name": "OrderFulfilled",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "bytes32",
                "name": "orderHash",
                "type": "bytes32",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "offerer",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "zone",
                "type": "address",
            },
        ],
        "name": "OrderValidated",
        "type": "event",
    },
    {
        "inputs": [
            {
                "components": [
                    {"internalType": "address", "name": "offerer", "type": "address"},
                    {"internalType": "address", "name": "zone", "type": "address"},
                    {
                        "components": [
                            {
                                "internalType": "enum ItemType",
                                "name": "itemType",
                                "type": "uint8",
                            },
                            {
                                "internalType": "address",
                                "name": "token",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "identifierOrCriteria",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startAmount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "endAmount",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct OfferItem[]",
                        "name": "offer",
                        "type": "tuple[]",
                    },
                    {
                        "components": [
                            {
                                "internalType": "enum ItemType",
                                "name": "itemType",
                                "type": "uint8",
                            },
                            {
                                "internalType": "address",
                                "name": "token",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "identifierOrCriteria",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startAmount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "endAmount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address payable",
                                "name": "recipient",
                                "type": "address",
                            },
                        ],
                        "internalType": "struct ConsiderationItem[]",
                        "name": "consideration",
                        "type": "tuple[]",
                    },
                    {
                        "internalType": "enum OrderType",
                        "name": "orderType",
                        "type": "uint8",
                    },
                    {"internalType": "uint256", "name": "startTime", "type": "uint256"},
                    {"internalType": "uint256", "name": "endTime", "type": "uint256"},
                    {"internalType": "bytes32", "name": "zoneHash", "type": "bytes32"},
                    {"internalType": "uint256", "name": "salt", "type": "uint256"},
                    {
                        "internalType": "bytes32",
                        "name": "conduitKey",
                        "type": "bytes32",
                    },
                    {"internalType": "uint256", "name": "counter", "type": "uint256"},
                ],
                "internalType": "struct OrderComponents[]",
                "name": "orders",
                "type": "tuple[]",
            }
        ],
        "name": "cancel",
        "outputs": [{"internalType": "bool", "name": "cancelled", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "components": [
                            {
                                "internalType": "address",
                                "name": "offerer",
                                "type": "address",
                            },
                            {
                                "internalType": "address",
                                "name": "zone",
                                "type": "address",
                            },
                            {
                                "components": [
                                    {
                                        "internalType": "enum ItemType",
                                        "name": "itemType",
                                        "type": "uint8",
                                    },
                                    {
                                        "internalType": "address",
                                        "name": "token",
                                        "type": "address",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "identifierOrCriteria",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "startAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "endAmount",
                                        "type": "uint256",
                                    },
                                ],
                                "internalType": "struct OfferItem[]",
                                "name": "offer",
                                "type": "tuple[]",
                            },
                            {
                                "components": [
                                    {
                                        "internalType": "enum ItemType",
                                        "name": "itemType",
                                        "type": "uint8",
                                    },
                                    {
                                        "internalType": "address",
                                        "name": "token",
                                        "type": "address",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "identifierOrCriteria",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "startAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "endAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "address payable",
                                        "name": "recipient",
                                        "type": "address",
                                    },
                                ],
                                "internalType": "struct ConsiderationItem[]",
                                "name": "consideration",
                                "type": "tuple[]",
                            },
                            {
                                "internalType": "enum OrderType",
                                "name": "orderType",
                                "type": "uint8",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "endTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "bytes32",
                                "name": "zoneHash",
                                "type": "bytes32",
                            },
                            {
                                "internalType": "uint256",
                                "name": "salt",
                                "type": "uint256",
                            },
                            {
                                "internalType": "bytes32",
                                "name": "conduitKey",
                                "type": "bytes32",
                            },
                            {
                                "internalType": "uint256",
                                "name": "totalOriginalConsiderationItems",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct OrderParameters",
                        "name": "parameters",
                        "type": "tuple",
                    },
                    {"internalType": "uint120", "name": "numerator", "type": "uint120"},
                    {
                        "internalType": "uint120",
                        "name": "denominator",
                        "type": "uint120",
                    },
                    {"internalType": "bytes", "name": "signature", "type": "bytes"},
                    {"internalType": "bytes", "name": "extraData", "type": "bytes"},
                ],
                "internalType": "struct AdvancedOrder",
                "name": "advancedOrder",
                "type": "tuple",
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "orderIndex",
                        "type": "uint256",
                    },
                    {"internalType": "enum Side", "name": "side", "type": "uint8"},
                    {"internalType": "uint256", "name": "index", "type": "uint256"},
                    {
                        "internalType": "uint256",
                        "name": "identifier",
                        "type": "uint256",
                    },
                    {
                        "internalType": "bytes32[]",
                        "name": "criteriaProof",
                        "type": "bytes32[]",
                    },
                ],
                "internalType": "struct CriteriaResolver[]",
                "name": "criteriaResolvers",
                "type": "tuple[]",
            },
            {
                "internalType": "bytes32",
                "name": "fulfillerConduitKey",
                "type": "bytes32",
            },
            {"internalType": "address", "name": "recipient", "type": "address"},
        ],
        "name": "fulfillAdvancedOrder",
        "outputs": [{"internalType": "bool", "name": "fulfilled", "type": "bool"}],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "components": [
                            {
                                "internalType": "address",
                                "name": "offerer",
                                "type": "address",
                            },
                            {
                                "internalType": "address",
                                "name": "zone",
                                "type": "address",
                            },
                            {
                                "components": [
                                    {
                                        "internalType": "enum ItemType",
                                        "name": "itemType",
                                        "type": "uint8",
                                    },
                                    {
                                        "internalType": "address",
                                        "name": "token",
                                        "type": "address",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "identifierOrCriteria",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "startAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "endAmount",
                                        "type": "uint256",
                                    },
                                ],
                                "internalType": "struct OfferItem[]",
                                "name": "offer",
                                "type": "tuple[]",
                            },
                            {
                                "components": [
                                    {
                                        "internalType": "enum ItemType",
                                        "name": "itemType",
                                        "type": "uint8",
                                    },
                                    {
                                        "internalType": "address",
                                        "name": "token",
                                        "type": "address",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "identifierOrCriteria",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "startAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "endAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "address payable",
                                        "name": "recipient",
                                        "type": "address",
                                    },
                                ],
                                "internalType": "struct ConsiderationItem[]",
                                "name": "consideration",
                                "type": "tuple[]",
                            },
                            {
                                "internalType": "enum OrderType",
                                "name": "orderType",
                                "type": "uint8",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "endTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "bytes32",
                                "name": "zoneHash",
                                "type": "bytes32",
                            },
                            {
                                "internalType": "uint256",
                                "name": "salt",
                                "type": "uint256",
                            },
                            {
                                "internalType": "bytes32",
                                "name": "conduitKey",
                                "type": "bytes32",
                            },
                            {
                                "internalType": "uint256",
                                "name": "totalOriginalConsiderationItems",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct OrderParameters",
                        "name": "parameters",
                        "type": "tuple",
                    },
                    {"internalType": "uint120", "name": "numerator", "type": "uint120"},
                    {
                        "internalType": "uint120",
                        "name": "denominator",
                        "type": "uint120",
                    },
                    {"internalType": "bytes", "name": "signature", "type": "bytes"},
                    {"internalType": "bytes", "name": "extraData", "type": "bytes"},
                ],
                "internalType": "struct AdvancedOrder[]",
                "name": "advancedOrders",
                "type": "tuple[]",
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "orderIndex",
                        "type": "uint256",
                    },
                    {"internalType": "enum Side", "name": "side", "type": "uint8"},
                    {"internalType": "uint256", "name": "index", "type": "uint256"},
                    {
                        "internalType": "uint256",
                        "name": "identifier",
                        "type": "uint256",
                    },
                    {
                        "internalType": "bytes32[]",
                        "name": "criteriaProof",
                        "type": "bytes32[]",
                    },
                ],
                "internalType": "struct CriteriaResolver[]",
                "name": "criteriaResolvers",
                "type": "tuple[]",
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "orderIndex",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "itemIndex", "type": "uint256"},
                ],
                "internalType": "struct FulfillmentComponent[][]",
                "name": "offerFulfillments",
                "type": "tuple[][]",
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "orderIndex",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "itemIndex", "type": "uint256"},
                ],
                "internalType": "struct FulfillmentComponent[][]",
                "name": "considerationFulfillments",
                "type": "tuple[][]",
            },
            {
                "internalType": "bytes32",
                "name": "fulfillerConduitKey",
                "type": "bytes32",
            },
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "maximumFulfilled", "type": "uint256"},
        ],
        "name": "fulfillAvailableAdvancedOrders",
        "outputs": [
            {"internalType": "bool[]", "name": "availableOrders", "type": "bool[]"},
            {
                "components": [
                    {
                        "components": [
                            {
                                "internalType": "enum ItemType",
                                "name": "itemType",
                                "type": "uint8",
                            },
                            {
                                "internalType": "address",
                                "name": "token",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "identifier",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "amount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address payable",
                                "name": "recipient",
                                "type": "address",
                            },
                        ],
                        "internalType": "struct ReceivedItem",
                        "name": "item",
                        "type": "tuple",
                    },
                    {"internalType": "address", "name": "offerer", "type": "address"},
                    {
                        "internalType": "bytes32",
                        "name": "conduitKey",
                        "type": "bytes32",
                    },
                ],
                "internalType": "struct Execution[]",
                "name": "executions",
                "type": "tuple[]",
            },
        ],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "components": [
                            {
                                "internalType": "address",
                                "name": "offerer",
                                "type": "address",
                            },
                            {
                                "internalType": "address",
                                "name": "zone",
                                "type": "address",
                            },
                            {
                                "components": [
                                    {
                                        "internalType": "enum ItemType",
                                        "name": "itemType",
                                        "type": "uint8",
                                    },
                                    {
                                        "internalType": "address",
                                        "name": "token",
                                        "type": "address",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "identifierOrCriteria",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "startAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "endAmount",
                                        "type": "uint256",
                                    },
                                ],
                                "internalType": "struct OfferItem[]",
                                "name": "offer",
                                "type": "tuple[]",
                            },
                            {
                                "components": [
                                    {
                                        "internalType": "enum ItemType",
                                        "name": "itemType",
                                        "type": "uint8",
                                    },
                                    {
                                        "internalType": "address",
                                        "name": "token",
                                        "type": "address",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "identifierOrCriteria",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "startAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "endAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "address payable",
                                        "name": "recipient",
                                        "type": "address",
                                    },
                                ],
                                "internalType": "struct ConsiderationItem[]",
                                "name": "consideration",
                                "type": "tuple[]",
                            },
                            {
                                "internalType": "enum OrderType",
                                "name": "orderType",
                                "type": "uint8",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "endTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "bytes32",
                                "name": "zoneHash",
                                "type": "bytes32",
                            },
                            {
                                "internalType": "uint256",
                                "name": "salt",
                                "type": "uint256",
                            },
                            {
                                "internalType": "bytes32",
                                "name": "conduitKey",
                                "type": "bytes32",
                            },
                            {
                                "internalType": "uint256",
                                "name": "totalOriginalConsiderationItems",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct OrderParameters",
                        "name": "parameters",
                        "type": "tuple",
                    },
                    {"internalType": "bytes", "name": "signature", "type": "bytes"},
                ],
                "internalType": "struct Order[]",
                "name": "orders",
                "type": "tuple[]",
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "orderIndex",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "itemIndex", "type": "uint256"},
                ],
                "internalType": "struct FulfillmentComponent[][]",
                "name": "offerFulfillments",
                "type": "tuple[][]",
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "orderIndex",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "itemIndex", "type": "uint256"},
                ],
                "internalType": "struct FulfillmentComponent[][]",
                "name": "considerationFulfillments",
                "type": "tuple[][]",
            },
            {
                "internalType": "bytes32",
                "name": "fulfillerConduitKey",
                "type": "bytes32",
            },
            {"internalType": "uint256", "name": "maximumFulfilled", "type": "uint256"},
        ],
        "name": "fulfillAvailableOrders",
        "outputs": [
            {"internalType": "bool[]", "name": "availableOrders", "type": "bool[]"},
            {
                "components": [
                    {
                        "components": [
                            {
                                "internalType": "enum ItemType",
                                "name": "itemType",
                                "type": "uint8",
                            },
                            {
                                "internalType": "address",
                                "name": "token",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "identifier",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "amount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address payable",
                                "name": "recipient",
                                "type": "address",
                            },
                        ],
                        "internalType": "struct ReceivedItem",
                        "name": "item",
                        "type": "tuple",
                    },
                    {"internalType": "address", "name": "offerer", "type": "address"},
                    {
                        "internalType": "bytes32",
                        "name": "conduitKey",
                        "type": "bytes32",
                    },
                ],
                "internalType": "struct Execution[]",
                "name": "executions",
                "type": "tuple[]",
            },
        ],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "address",
                        "name": "considerationToken",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "considerationIdentifier",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "considerationAmount",
                        "type": "uint256",
                    },
                    {
                        "internalType": "address payable",
                        "name": "offerer",
                        "type": "address",
                    },
                    {"internalType": "address", "name": "zone", "type": "address"},
                    {
                        "internalType": "address",
                        "name": "offerToken",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "offerIdentifier",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "offerAmount",
                        "type": "uint256",
                    },
                    {
                        "internalType": "enum BasicOrderType",
                        "name": "basicOrderType",
                        "type": "uint8",
                    },
                    {"internalType": "uint256", "name": "startTime", "type": "uint256"},
                    {"internalType": "uint256", "name": "endTime", "type": "uint256"},
                    {"internalType": "bytes32", "name": "zoneHash", "type": "bytes32"},
                    {"internalType": "uint256", "name": "salt", "type": "uint256"},
                    {
                        "internalType": "bytes32",
                        "name": "offererConduitKey",
                        "type": "bytes32",
                    },
                    {
                        "internalType": "bytes32",
                        "name": "fulfillerConduitKey",
                        "type": "bytes32",
                    },
                    {
                        "internalType": "uint256",
                        "name": "totalOriginalAdditionalRecipients",
                        "type": "uint256",
                    },
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "amount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address payable",
                                "name": "recipient",
                                "type": "address",
                            },
                        ],
                        "internalType": "struct AdditionalRecipient[]",
                        "name": "additionalRecipients",
                        "type": "tuple[]",
                    },
                    {"internalType": "bytes", "name": "signature", "type": "bytes"},
                ],
                "internalType": "struct BasicOrderParameters",
                "name": "parameters",
                "type": "tuple",
            }
        ],
        "name": "fulfillBasicOrder",
        "outputs": [{"internalType": "bool", "name": "fulfilled", "type": "bool"}],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "components": [
                            {
                                "internalType": "address",
                                "name": "offerer",
                                "type": "address",
                            },
                            {
                                "internalType": "address",
                                "name": "zone",
                                "type": "address",
                            },
                            {
                                "components": [
                                    {
                                        "internalType": "enum ItemType",
                                        "name": "itemType",
                                        "type": "uint8",
                                    },
                                    {
                                        "internalType": "address",
                                        "name": "token",
                                        "type": "address",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "identifierOrCriteria",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "startAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "endAmount",
                                        "type": "uint256",
                                    },
                                ],
                                "internalType": "struct OfferItem[]",
                                "name": "offer",
                                "type": "tuple[]",
                            },
                            {
                                "components": [
                                    {
                                        "internalType": "enum ItemType",
                                        "name": "itemType",
                                        "type": "uint8",
                                    },
                                    {
                                        "internalType": "address",
                                        "name": "token",
                                        "type": "address",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "identifierOrCriteria",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "startAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "endAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "address payable",
                                        "name": "recipient",
                                        "type": "address",
                                    },
                                ],
                                "internalType": "struct ConsiderationItem[]",
                                "name": "consideration",
                                "type": "tuple[]",
                            },
                            {
                                "internalType": "enum OrderType",
                                "name": "orderType",
                                "type": "uint8",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "endTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "bytes32",
                                "name": "zoneHash",
                                "type": "bytes32",
                            },
                            {
                                "internalType": "uint256",
                                "name": "salt",
                                "type": "uint256",
                            },
                            {
                                "internalType": "bytes32",
                                "name": "conduitKey",
                                "type": "bytes32",
                            },
                            {
                                "internalType": "uint256",
                                "name": "totalOriginalConsiderationItems",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct OrderParameters",
                        "name": "parameters",
                        "type": "tuple",
                    },
                    {"internalType": "bytes", "name": "signature", "type": "bytes"},
                ],
                "internalType": "struct Order",
                "name": "order",
                "type": "tuple",
            },
            {
                "internalType": "bytes32",
                "name": "fulfillerConduitKey",
                "type": "bytes32",
            },
        ],
        "name": "fulfillOrder",
        "outputs": [{"internalType": "bool", "name": "fulfilled", "type": "bool"}],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "offerer", "type": "address"}],
        "name": "getCounter",
        "outputs": [{"internalType": "uint256", "name": "counter", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {"internalType": "address", "name": "offerer", "type": "address"},
                    {"internalType": "address", "name": "zone", "type": "address"},
                    {
                        "components": [
                            {
                                "internalType": "enum ItemType",
                                "name": "itemType",
                                "type": "uint8",
                            },
                            {
                                "internalType": "address",
                                "name": "token",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "identifierOrCriteria",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startAmount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "endAmount",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct OfferItem[]",
                        "name": "offer",
                        "type": "tuple[]",
                    },
                    {
                        "components": [
                            {
                                "internalType": "enum ItemType",
                                "name": "itemType",
                                "type": "uint8",
                            },
                            {
                                "internalType": "address",
                                "name": "token",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "identifierOrCriteria",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startAmount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "endAmount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address payable",
                                "name": "recipient",
                                "type": "address",
                            },
                        ],
                        "internalType": "struct ConsiderationItem[]",
                        "name": "consideration",
                        "type": "tuple[]",
                    },
                    {
                        "internalType": "enum OrderType",
                        "name": "orderType",
                        "type": "uint8",
                    },
                    {"internalType": "uint256", "name": "startTime", "type": "uint256"},
                    {"internalType": "uint256", "name": "endTime", "type": "uint256"},
                    {"internalType": "bytes32", "name": "zoneHash", "type": "bytes32"},
                    {"internalType": "uint256", "name": "salt", "type": "uint256"},
                    {
                        "internalType": "bytes32",
                        "name": "conduitKey",
                        "type": "bytes32",
                    },
                    {"internalType": "uint256", "name": "counter", "type": "uint256"},
                ],
                "internalType": "struct OrderComponents",
                "name": "order",
                "type": "tuple",
            }
        ],
        "name": "getOrderHash",
        "outputs": [
            {"internalType": "bytes32", "name": "orderHash", "type": "bytes32"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "bytes32", "name": "orderHash", "type": "bytes32"}],
        "name": "getOrderStatus",
        "outputs": [
            {"internalType": "bool", "name": "isValidated", "type": "bool"},
            {"internalType": "bool", "name": "isCancelled", "type": "bool"},
            {"internalType": "uint256", "name": "totalFilled", "type": "uint256"},
            {"internalType": "uint256", "name": "totalSize", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "incrementCounter",
        "outputs": [
            {"internalType": "uint256", "name": "newCounter", "type": "uint256"}
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "information",
        "outputs": [
            {"internalType": "string", "name": "version", "type": "string"},
            {"internalType": "bytes32", "name": "domainSeparator", "type": "bytes32"},
            {"internalType": "address", "name": "conduitController", "type": "address"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "components": [
                            {
                                "internalType": "address",
                                "name": "offerer",
                                "type": "address",
                            },
                            {
                                "internalType": "address",
                                "name": "zone",
                                "type": "address",
                            },
                            {
                                "components": [
                                    {
                                        "internalType": "enum ItemType",
                                        "name": "itemType",
                                        "type": "uint8",
                                    },
                                    {
                                        "internalType": "address",
                                        "name": "token",
                                        "type": "address",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "identifierOrCriteria",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "startAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "endAmount",
                                        "type": "uint256",
                                    },
                                ],
                                "internalType": "struct OfferItem[]",
                                "name": "offer",
                                "type": "tuple[]",
                            },
                            {
                                "components": [
                                    {
                                        "internalType": "enum ItemType",
                                        "name": "itemType",
                                        "type": "uint8",
                                    },
                                    {
                                        "internalType": "address",
                                        "name": "token",
                                        "type": "address",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "identifierOrCriteria",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "startAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "endAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "address payable",
                                        "name": "recipient",
                                        "type": "address",
                                    },
                                ],
                                "internalType": "struct ConsiderationItem[]",
                                "name": "consideration",
                                "type": "tuple[]",
                            },
                            {
                                "internalType": "enum OrderType",
                                "name": "orderType",
                                "type": "uint8",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "endTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "bytes32",
                                "name": "zoneHash",
                                "type": "bytes32",
                            },
                            {
                                "internalType": "uint256",
                                "name": "salt",
                                "type": "uint256",
                            },
                            {
                                "internalType": "bytes32",
                                "name": "conduitKey",
                                "type": "bytes32",
                            },
                            {
                                "internalType": "uint256",
                                "name": "totalOriginalConsiderationItems",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct OrderParameters",
                        "name": "parameters",
                        "type": "tuple",
                    },
                    {"internalType": "uint120", "name": "numerator", "type": "uint120"},
                    {
                        "internalType": "uint120",
                        "name": "denominator",
                        "type": "uint120",
                    },
                    {"internalType": "bytes", "name": "signature", "type": "bytes"},
                    {"internalType": "bytes", "name": "extraData", "type": "bytes"},
                ],
                "internalType": "struct AdvancedOrder[]",
                "name": "advancedOrders",
                "type": "tuple[]",
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "orderIndex",
                        "type": "uint256",
                    },
                    {"internalType": "enum Side", "name": "side", "type": "uint8"},
                    {"internalType": "uint256", "name": "index", "type": "uint256"},
                    {
                        "internalType": "uint256",
                        "name": "identifier",
                        "type": "uint256",
                    },
                    {
                        "internalType": "bytes32[]",
                        "name": "criteriaProof",
                        "type": "bytes32[]",
                    },
                ],
                "internalType": "struct CriteriaResolver[]",
                "name": "criteriaResolvers",
                "type": "tuple[]",
            },
            {
                "components": [
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "orderIndex",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "itemIndex",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct FulfillmentComponent[]",
                        "name": "offerComponents",
                        "type": "tuple[]",
                    },
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "orderIndex",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "itemIndex",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct FulfillmentComponent[]",
                        "name": "considerationComponents",
                        "type": "tuple[]",
                    },
                ],
                "internalType": "struct Fulfillment[]",
                "name": "fulfillments",
                "type": "tuple[]",
            },
        ],
        "name": "matchAdvancedOrders",
        "outputs": [
            {
                "components": [
                    {
                        "components": [
                            {
                                "internalType": "enum ItemType",
                                "name": "itemType",
                                "type": "uint8",
                            },
                            {
                                "internalType": "address",
                                "name": "token",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "identifier",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "amount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address payable",
                                "name": "recipient",
                                "type": "address",
                            },
                        ],
                        "internalType": "struct ReceivedItem",
                        "name": "item",
                        "type": "tuple",
                    },
                    {"internalType": "address", "name": "offerer", "type": "address"},
                    {
                        "internalType": "bytes32",
                        "name": "conduitKey",
                        "type": "bytes32",
                    },
                ],
                "internalType": "struct Execution[]",
                "name": "executions",
                "type": "tuple[]",
            }
        ],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "components": [
                            {
                                "internalType": "address",
                                "name": "offerer",
                                "type": "address",
                            },
                            {
                                "internalType": "address",
                                "name": "zone",
                                "type": "address",
                            },
                            {
                                "components": [
                                    {
                                        "internalType": "enum ItemType",
                                        "name": "itemType",
                                        "type": "uint8",
                                    },
                                    {
                                        "internalType": "address",
                                        "name": "token",
                                        "type": "address",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "identifierOrCriteria",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "startAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "endAmount",
                                        "type": "uint256",
                                    },
                                ],
                                "internalType": "struct OfferItem[]",
                                "name": "offer",
                                "type": "tuple[]",
                            },
                            {
                                "components": [
                                    {
                                        "internalType": "enum ItemType",
                                        "name": "itemType",
                                        "type": "uint8",
                                    },
                                    {
                                        "internalType": "address",
                                        "name": "token",
                                        "type": "address",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "identifierOrCriteria",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "startAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "endAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "address payable",
                                        "name": "recipient",
                                        "type": "address",
                                    },
                                ],
                                "internalType": "struct ConsiderationItem[]",
                                "name": "consideration",
                                "type": "tuple[]",
                            },
                            {
                                "internalType": "enum OrderType",
                                "name": "orderType",
                                "type": "uint8",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "endTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "bytes32",
                                "name": "zoneHash",
                                "type": "bytes32",
                            },
                            {
                                "internalType": "uint256",
                                "name": "salt",
                                "type": "uint256",
                            },
                            {
                                "internalType": "bytes32",
                                "name": "conduitKey",
                                "type": "bytes32",
                            },
                            {
                                "internalType": "uint256",
                                "name": "totalOriginalConsiderationItems",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct OrderParameters",
                        "name": "parameters",
                        "type": "tuple",
                    },
                    {"internalType": "bytes", "name": "signature", "type": "bytes"},
                ],
                "internalType": "struct Order[]",
                "name": "orders",
                "type": "tuple[]",
            },
            {
                "components": [
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "orderIndex",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "itemIndex",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct FulfillmentComponent[]",
                        "name": "offerComponents",
                        "type": "tuple[]",
                    },
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "orderIndex",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "itemIndex",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct FulfillmentComponent[]",
                        "name": "considerationComponents",
                        "type": "tuple[]",
                    },
                ],
                "internalType": "struct Fulfillment[]",
                "name": "fulfillments",
                "type": "tuple[]",
            },
        ],
        "name": "matchOrders",
        "outputs": [
            {
                "components": [
                    {
                        "components": [
                            {
                                "internalType": "enum ItemType",
                                "name": "itemType",
                                "type": "uint8",
                            },
                            {
                                "internalType": "address",
                                "name": "token",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "identifier",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "amount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address payable",
                                "name": "recipient",
                                "type": "address",
                            },
                        ],
                        "internalType": "struct ReceivedItem",
                        "name": "item",
                        "type": "tuple",
                    },
                    {"internalType": "address", "name": "offerer", "type": "address"},
                    {
                        "internalType": "bytes32",
                        "name": "conduitKey",
                        "type": "bytes32",
                    },
                ],
                "internalType": "struct Execution[]",
                "name": "executions",
                "type": "tuple[]",
            }
        ],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [
            {"internalType": "string", "name": "contractName", "type": "string"}
        ],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "components": [
                            {
                                "internalType": "address",
                                "name": "offerer",
                                "type": "address",
                            },
                            {
                                "internalType": "address",
                                "name": "zone",
                                "type": "address",
                            },
                            {
                                "components": [
                                    {
                                        "internalType": "enum ItemType",
                                        "name": "itemType",
                                        "type": "uint8",
                                    },
                                    {
                                        "internalType": "address",
                                        "name": "token",
                                        "type": "address",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "identifierOrCriteria",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "startAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "endAmount",
                                        "type": "uint256",
                                    },
                                ],
                                "internalType": "struct OfferItem[]",
                                "name": "offer",
                                "type": "tuple[]",
                            },
                            {
                                "components": [
                                    {
                                        "internalType": "enum ItemType",
                                        "name": "itemType",
                                        "type": "uint8",
                                    },
                                    {
                                        "internalType": "address",
                                        "name": "token",
                                        "type": "address",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "identifierOrCriteria",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "startAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "endAmount",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "address payable",
                                        "name": "recipient",
                                        "type": "address",
                                    },
                                ],
                                "internalType": "struct ConsiderationItem[]",
                                "name": "consideration",
                                "type": "tuple[]",
                            },
                            {
                                "internalType": "enum OrderType",
                                "name": "orderType",
                                "type": "uint8",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "endTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "bytes32",
                                "name": "zoneHash",
                                "type": "bytes32",
                            },
                            {
                                "internalType": "uint256",
                                "name": "salt",
                                "type": "uint256",
                            },
                            {
                                "internalType": "bytes32",
                                "name": "conduitKey",
                                "type": "bytes32",
                            },
                            {
                                "internalType": "uint256",
                                "name": "totalOriginalConsiderationItems",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct OrderParameters",
                        "name": "parameters",
                        "type": "tuple",
                    },
                    {"internalType": "bytes", "name": "signature", "type": "bytes"},
                ],
                "internalType": "struct Order[]",
                "name": "orders",
                "type": "tuple[]",
            }
        ],
        "name": "validate",
        "outputs": [{"internalType": "bool", "name": "validated", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]
