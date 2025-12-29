# Threat Model: Suspicious Profile Analyzer

## Types of Fake Profiles

### Romance Scam Profiles
**Characteristics**: Attractive stolen photos, emotional backstories, claims of military deployment or overseas work
**Behavior**: Build emotional connections over weeks/months before requesting emergency financial assistance
**Platforms**: Dating apps (Tinder, Bumble), social media (Facebook, Instagram)
**Detection Indicators**: New accounts, professional photos, urgent financial language combined with emotional appeals

### Job Fraud Profiles
**Characteristics**: Professional headshots, fake company credentials, urgent hiring language
**Behavior**: Post fake job listings, request personal information during fake application processes
**Platforms**: LinkedIn, Indeed, job boards, professional networks
**Detection Indicators**: Incomplete company profiles, requests for SSN/banking info, upfront payment requirements

### Phishing/Social Engineering Profiles
**Characteristics**: Impersonate trusted entities (banks, tech support, government agencies)
**Behavior**: Send urgent messages requesting account verification, password resets, or security updates
**Platforms**: All platforms, often targeting specific demographics or recent data breach victims
**Detection Indicators**: Authority impersonation, urgency language, external links to suspicious domains

### Bot Networks/Coordinated Inauthentic Behavior
**Characteristics**: Similar profile patterns, synchronized posting schedules, generic stock photos
**Behavior**: Amplify misinformation, manipulate trending topics, spam promotional links
**Platforms**: Twitter, Facebook, Instagram, TikTok
**Detection Indicators**: Identical posting patterns, rapid account creation, abnormal follower ratios

### Identity Impersonation Profiles
**Characteristics**: Stolen photos and personal details from real people's social media accounts
**Behavior**: Damage victim reputation, catfish romantic targets, commit fraud using stolen identity
**Platforms**: All social platforms, dating apps, professional networks
**Detection Indicators**: Reverse image search hits, inconsistent personal details, geographic impossibilities

## Attacker Goals

### Financial Exploitation
- **Direct Theft**: Request wire transfers, gift cards, cryptocurrency payments for fake emergencies
- **Credential Harvesting**: Steal banking login information, credit card numbers, tax documents
- **Identity Theft**: Collect SSNs, addresses, mother's maiden names for loan fraud and account takeovers

### Data Collection
- **Personal Information**: Phone numbers, addresses, family details for future targeting
- **Professional Intelligence**: Company information, trade secrets, client lists for corporate espionage
- **Authentication Data**: Passwords, security questions, two-factor authentication codes

### Reputation Damage
- **Individual Targeting**: Impersonate victims to damage personal relationships or career prospects
- **Corporate Sabotage**: Create fake employee profiles to spread negative information about companies
- **Political Manipulation**: Influence elections and public opinion through coordinated disinformation

## Attack Vectors

### Direct Messaging Campaigns
- **Romance Manipulation**: "I'm deployed overseas and need emergency funds for medical treatment"
- **Job Fraud**: "Congratulations! You're hired. Send your SSN for the background check process"
- **Authority Impersonation**: "Your account is compromised. Click here immediately to secure it"

### Fake Content Creation
- **Fraudulent Job Postings**: High-paying remote work requiring upfront equipment payments
- **Investment Scams**: Cryptocurrency opportunities, fake trading platforms with guaranteed returns
- **Emergency Appeals**: Fake charity drives, disaster relief scams exploiting current events

### Social Engineering Tactics
- **Trust Building**: Months of relationship development before financial exploitation begins
- **Authority Exploitation**: Pose as HR representatives, IT support, government officials
- **Urgency Creation**: "Limited time offer" or "account will be closed" pressure tactics

### Network Infiltration
- **Connection Farming**: Build large follower bases to appear legitimate and trustworthy
- **Mutual Friend Exploitation**: Target friends of already-compromised accounts for credibility
- **Professional Network Abuse**: Use LinkedIn connections and endorsements for false credibility

## Impact Assessment

### Individual User Impact
- **Financial Losses**: Average romance scam loss of $2,400 per victim, with some losing life savings
- **Identity Theft**: Credit score damage, fraudulent accounts opened, legal complications from stolen identity
- **Emotional Trauma**: Depression, anxiety, loss of trust in online relationships and digital interactions
- **Professional Damage**: Career harm from leaked personal information or damaged professional reputation

### Platform Impact
- **User Trust Erosion**: Decreased engagement, account deletions, negative reviews and media coverage
- **Legal and Regulatory Liability**: Fines from regulators, lawsuits from affected users and their families
- **Operational Costs**: Increased manual moderation, customer support, fraud investigation resources
- **Brand Reputation Damage**: Media coverage of successful scams permanently damages platform credibility

### Societal Impact
- **Economic Losses**: $1.3 billion in annual losses from romance scams alone, billions more from other fraud types
- **Democratic Interference**: Election manipulation through coordinated disinformation and fake grassroots movements
- **Social Cohesion Erosion**: Decreased trust in online interactions, digital platforms, and remote relationships
- **Vulnerable Population Targeting**: Elderly, isolated, and financially desperate individuals disproportionately harmed