# blockchain pros & cons (mostly cons)

## pros
- immutable
- distributed
- trustless tamper evidence

## cons
- proof of work wastes too much energy
- need for incentives to convince nodes to participate in the mining/verification process which leads to imbalance of power and/or resources (the rich get richer because they can afford to participate more effectively)
- whales
- mining pools control majority of the mining power
- high gas fees
- any consensus algorithm on a permissionless blockchain adds non-negligible overhead to the efficiency of the network
- blockchain transactions will always be slower and less efficient compared to a trusted and centralized third party because of the overhead of byzantine consensus
- centralized databases are cheaper, faster and easier to work with even when the size of the data becomes imparctical for most nodes on a permissionless blockchain
- in order for a network to be truly trustless, every node needs to download the entire blockchain (bitcoin is approaching 400gb)
- does not scale well
- storage on the blockchain is very expnensive (november 2021: it costs roughly $7.50 to store a single 256-bit integer on the Ethereum blockchain)
- querying data from the blockchain is difficult (and thus centrallized, trusted parties emerge that do it for you)
- the oracle problem and unsatisfactory solutions (even in a trustless decentralized oracle, what if majority of the nodes of decide that their favourite did not lose the match?)
- enforement of the blockchain outside the network happens through a trusted third-party
- bugs in smart contracts are hard to fix in time
- no room for interpretation in smart contracts (respecting the letter of law but not its spirit. if code is law, theft by bugs/exploits are legal)
- inevitable centralization araound a convenient service (metamask, opensea, coinbase, etherscan)
- most interactions occur by calling apis provided by trusted centralized companies (infura, quicknode)
- 51% attacks (especially on smaller networks)
- most people don’t want to run their own servers/nodes
- permissionless blockchain is not an optimized solution for any real problem except that of evading the law
- unlike most internet protocols, in blockchain, most of the value lies at the protocol layer instead of the application layer
- abused the words 'crypto' and 'web 3.0' :(
- solidity is a boring language
- leads to the development of even more javascript frameworks
- on top of the time it takes for a block to be verified, it is probably still wrong and only probably right 6-8 transactions after
- network partition events (with no available solutions. (CAP theorem))
- in 2016, the creators of ethereum wrote a smart contract for "The DAO" in which bug allowed an attacker to drain so much money that the creators forked the entire network to essentially undo/reset it to before the attack. (wasn't blockchain supposed to be immuatable and hard to undo/overwite?)
