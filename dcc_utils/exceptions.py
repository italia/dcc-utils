class DCCError(Exception):
    pass


class DCCParsingError(DCCError):
    pass


class DCCSignatureError(DCCError):
    pass


class DCCRuleError(DCCError):
    pass
