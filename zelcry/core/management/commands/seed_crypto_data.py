from django.core.management.base import BaseCommand
from zelcry.core.models import CryptoAssetDetails


class Command(BaseCommand):
    help = 'Seed the database with top 20 cryptocurrency impact scores'

    def handle(self, *args, **kwargs):
        crypto_data = [
            {
                'coin_id': 'bitcoin',
                'name': 'Bitcoin',
                'symbol': 'BTC',
                'energy_score': 3,
                'governance_score': 8,
                'utility_score': 9,
                'description': 'Bitcoin is the first and most well-known cryptocurrency, created in 2009. It operates on a proof-of-work consensus mechanism.'
            },
            {
                'coin_id': 'ethereum',
                'name': 'Ethereum',
                'symbol': 'ETH',
                'energy_score': 8,
                'governance_score': 7,
                'utility_score': 10,
                'description': 'Ethereum is a decentralized platform for smart contracts and decentralized applications. It recently transitioned to proof-of-stake.'
            },
            {
                'coin_id': 'cardano',
                'name': 'Cardano',
                'symbol': 'ADA',
                'energy_score': 9,
                'governance_score': 9,
                'utility_score': 8,
                'description': 'Cardano is a proof-of-stake blockchain platform focused on sustainability and scalability, with strong academic research foundation.'
            },
            {
                'coin_id': 'solana',
                'name': 'Solana',
                'symbol': 'SOL',
                'energy_score': 7,
                'governance_score': 6,
                'utility_score': 9,
                'description': 'Solana is a high-performance blockchain known for fast transaction speeds and low fees, popular for DeFi and NFT applications.'
            },
            {
                'coin_id': 'polkadot',
                'name': 'Polkadot',
                'symbol': 'DOT',
                'energy_score': 8,
                'governance_score': 9,
                'utility_score': 8,
                'description': 'Polkadot is a multi-chain platform that enables different blockchains to interoperate and share information securely.'
            },
            {
                'coin_id': 'binancecoin',
                'name': 'BNB',
                'symbol': 'BNB',
                'energy_score': 7,
                'governance_score': 5,
                'utility_score': 9,
                'description': 'BNB is the native token of the Binance ecosystem, used for trading fees and powering the BNB Chain.'
            },
            {
                'coin_id': 'ripple',
                'name': 'XRP',
                'symbol': 'XRP',
                'energy_score': 9,
                'governance_score': 4,
                'utility_score': 8,
                'description': 'XRP is designed for fast, low-cost international payments and is used by financial institutions worldwide.'
            },
            {
                'coin_id': 'dogecoin',
                'name': 'Dogecoin',
                'symbol': 'DOGE',
                'energy_score': 4,
                'governance_score': 6,
                'utility_score': 5,
                'description': 'Dogecoin started as a meme cryptocurrency but has grown into a popular community-driven digital currency.'
            },
            {
                'coin_id': 'tron',
                'name': 'TRON',
                'symbol': 'TRX',
                'energy_score': 7,
                'governance_score': 6,
                'utility_score': 7,
                'description': 'TRON is a blockchain platform focused on building a decentralized internet and digital entertainment ecosystem.'
            },
            {
                'coin_id': 'chainlink',
                'name': 'Chainlink',
                'symbol': 'LINK',
                'energy_score': 8,
                'governance_score': 7,
                'utility_score': 9,
                'description': 'Chainlink is a decentralized oracle network that connects smart contracts with real-world data.'
            },
            {
                'coin_id': 'avalanche-2',
                'name': 'Avalanche',
                'symbol': 'AVAX',
                'energy_score': 9,
                'governance_score': 8,
                'utility_score': 8,
                'description': 'Avalanche is a fast, eco-friendly blockchain platform for decentralized applications and custom blockchain networks.'
            },
            {
                'coin_id': 'polygon',
                'name': 'Polygon',
                'symbol': 'MATIC',
                'energy_score': 8,
                'governance_score': 7,
                'utility_score': 9,
                'description': 'Polygon is a scaling solution for Ethereum, offering faster and cheaper transactions while maintaining security.'
            },
            {
                'coin_id': 'stellar',
                'name': 'Stellar',
                'symbol': 'XLM',
                'energy_score': 9,
                'governance_score': 7,
                'utility_score': 7,
                'description': 'Stellar is designed for fast, low-cost cross-border payments and financial inclusion.'
            },
            {
                'coin_id': 'algorand',
                'name': 'Algorand',
                'symbol': 'ALGO',
                'energy_score': 10,
                'governance_score': 8,
                'utility_score': 8,
                'description': 'Algorand is a carbon-negative blockchain that focuses on speed, security, and decentralization with pure proof-of-stake.'
            },
            {
                'coin_id': 'uniswap',
                'name': 'Uniswap',
                'symbol': 'UNI',
                'energy_score': 8,
                'governance_score': 9,
                'utility_score': 9,
                'description': 'Uniswap is the largest decentralized exchange protocol on Ethereum, enabling permissionless token swaps.'
            },
            {
                'coin_id': 'cosmos',
                'name': 'Cosmos',
                'symbol': 'ATOM',
                'energy_score': 8,
                'governance_score': 9,
                'utility_score': 8,
                'description': 'Cosmos is an ecosystem of interconnected blockchains designed to scale and interoperate with each other.'
            },
            {
                'coin_id': 'litecoin',
                'name': 'Litecoin',
                'symbol': 'LTC',
                'energy_score': 4,
                'governance_score': 6,
                'utility_score': 7,
                'description': 'Litecoin is a peer-to-peer cryptocurrency created as the silver to Bitcoin\'s gold, offering faster transaction times.'
            },
            {
                'coin_id': 'hedera-hashgraph',
                'name': 'Hedera',
                'symbol': 'HBAR',
                'energy_score': 10,
                'governance_score': 6,
                'utility_score': 8,
                'description': 'Hedera is an enterprise-grade public network using hashgraph consensus, known for its energy efficiency.'
            },
            {
                'coin_id': 'internet-computer',
                'name': 'Internet Computer',
                'symbol': 'ICP',
                'energy_score': 7,
                'governance_score': 7,
                'utility_score': 7,
                'description': 'Internet Computer is a blockchain that aims to extend the functionality of the internet with smart contracts.'
            },
            {
                'coin_id': 'near',
                'name': 'NEAR Protocol',
                'symbol': 'NEAR',
                'energy_score': 9,
                'governance_score': 8,
                'utility_score': 8,
                'description': 'NEAR is a climate-neutral, sharded proof-of-stake blockchain designed for usability and scalability.'
            }
        ]

        for data in crypto_data:
            crypto, created = CryptoAssetDetails.objects.update_or_create(
                coin_id=data['coin_id'],
                defaults={
                    'name': data['name'],
                    'symbol': data['symbol'],
                    'energy_score': data['energy_score'],
                    'governance_score': data['governance_score'],
                    'utility_score': data['utility_score'],
                    'description': data['description']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created {crypto.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Updated {crypto.name}'))

        self.stdout.write(self.style.SUCCESS('Successfully seeded crypto data!'))
