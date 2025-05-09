# Task 1.1 - Software Faults 

Written By: Suvansh Shukla (matriculation number: 256245)

## Crowdstrike Falcon

### What happened

In July 2024, a faulty software update to a popular and highly used cyber security software caused crashes and faults on millions of devices.

There were multiple different kinds of faults found among which the most common type of fault was a "Blue Screen Of Death". The update that caused this fault primarily affected machines running Microsoft Windows.

The outages and faults were extremely widespread with [8.5 million devices being affected](https://www.reuters.com/technology/crowdstrike-exec-apologize-faulty-update-that-caused-global-it-outage-2024-09-24/) 

### What was the cause

The cause as it turns out was an [improper content configuration update](https://www.crowdstrike.com/en-us/blog/falcon-content-update-preliminary-post-incident-report/) that caused this fault. The update was meant to gather telemetry information which would then be used to find new threat techniques.

### What were the consequences

Not only were over 8.5 million devices affect with crashes, BSODs and freezing. Many ciritical systems were also halted. Airlines cancelled their flights as well, for example [Delta airlines had to cancel over 7000 flights ](https://www.theguardian.com/technology/article/2024/jul/25/crowdstrike-workers-ubereats-vouchers), [health care services in the UK faced widespread disruptions](https://www.lemonde.fr/en/pixels/article/2024/07/19/airports-banks-and-hospitals-disrupted-by-biggest-it-outage-in-history_6690699_13.html) and media outlets across the US, UK and France couldn't broadcast either. 

Such outages and disruptions not only had an economic effect, they may very well also have led to human fatalities, due to certain patients not receiving critical care on time.

### How this may have been avoided

Such faults can rarely be attributed to single root causes. Only systemic mistakes and blindspots can really let such a far reaching fault go through the cracks of a fairly large and [competent company](https://www.crowdstrike.com/en-us/blog/crowdstrike-wins-2025-google-cloud-security-partner-of-the-year-award/) like crowdstrike.

In my opinion, better and more thorough testing protocols could have been added to catch such faults before shipping or deploying the changes. Better and more thorough code reviews should also be done to catch such possibilities during the development stage itself.

Certain steps can also be taken on the consumer part of the equation as well. Where airline companies can set policies to personally test and vet all updates before allowing the on their own devices to pull and incorporate the new changes. 

### Special considerations

The software CrowdStrike Falcon is fairly well made an [doesn't have a lot of competition](https://www.sangfor.com/blog/cybersecurity/15-top-endpoint-detection-and-response-edr-solutions#:~:text=to%20choose%20from.-,3.%20crowdstrike%20falcon,-Widely%20known%20as) in the field it operates or in the features it provides. I believe that working on alternatives to such kinds of software and perhaps making them open source could provide consumers more robust and cheaper alternatives.

Although [privileged access](https://theconversation.com/what-is-crowdstrike-falcon-and-what-does-it-do-is-my-computer-safe-235123) or kernel level access may be necessary for software such as crowdstrike falcon to function properly we can also consider revoking kernel level access and maybe incorporate it's basic functionality in the OS instead. This would reduces chances of such faults ever occurring due to third party software. 
