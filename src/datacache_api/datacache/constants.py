from .enums import enum

FILTER_TYPE = enum(
    NFT_PRIZE_IN_USDC='NFT_PRIZE_IN_USDC',
    NONE=''
)

FILTER_TYPE_CHOICES = [
    (FILTER_TYPE.NFT_PRIZE_IN_USDC, 'NFT Prize in USDC'),
    (FILTER_TYPE.NONE, 'None'),
]