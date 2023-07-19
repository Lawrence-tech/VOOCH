# VOOCH Project


## Description
The project is designed for clients involved in OOH advertising, including advertisers, marketing agencies, and businesses seeking to promote their products or services through billboards, bus shelters, and digital signage. 

The primary goal was to create a seamless user experience that allowed advertisers, marketing agencies, and businesses to preview their OOH artworks, select locations, and test them with the target market.
 
  


![Screenshot (39)](https://vooch.netlify.app/)





## Table of Contents
- Features
- Installation
- Technology stack
- Challenge
- Risks
- Authors
- Conclusion

## Features
Here's an overview of how VOOHC works:

Upload Artworks: Clients can easily upload their approved OOH artworks to the VOOHC platform.
The supported file formats may include common image formats such as JPEG, PNG, or even design files like 
Adobe Photoshop (PSD) or Illustrator (AI).


Select Locations: Once the artwork is uploaded, clients can choose from a database of predefined OOH locations or 
provide specific GPS coordinates for custom locations. These locations represent real-world settings where the OOH 
ads will be displayed, such as billboards, bus shelters, or digital signage.


Visualize Artworks: VOOHC uses advanced image manipulation techniques to superimpose the uploaded artwork onto the
selected OOH locations. The client can then preview how the artwork will appear in different contexts, helping them
make informed decisions about design, placement, and overall impact.


Target Market Testing: In addition to visualizing the artwork in different settings, VOOHC provides a feature for 
testing the artworks with the target market. The client can define specific demographics or audience characteristics 
to simulate the real-world impact of the artwork. The application generates a simulated response or feedback based on
the selected target market, helping the client gauge the effectiveness of their OOH campaign.


Instant Feedback: VOOHC offers immediate feedback on the artwork, taking into account the target market's response.
Clients can receive data and analytics about the simulated impact, including impressions, engagement rates, or even 
sentiment analysis. This feedback can guide further adjustments or optimizations to maximize the effectiveness of the OOH campaign.

Printing and Implementation: Once the client is satisfied with the visualized artwork and feedback, they can proceed
with the printing and implementation of the OOH campaign. VOOHC can assist in providing print-ready files or connect 
clients with printing partners for a seamless transition from the digital preview to real-world advertising.

By utilizing VOOHC, clients can save time and resources by visualizing their OOH artworks before printing, testing them
with their target market, and making data-driven decisions for their advertising campaigns. The application empowers clients 
to optimize their OOH creatives for maximum impact and enhances the overall effectiveness of their marketing efforts.


### Pre-Designed Pages
ℹ️ Home/About Page  
📄 Sign In
📝 Pricing 
🗂️ Upload 
📄 Features
📄 Platform
📞 Contact us   

## Installation
### Local development 🔧
##### Clone the repository
`git@github.com:Lawrence-tech/VOOCH.git`

##### Cd in the project directory
$ `cd VOOCH/`

##### Start local dev server
$ `environments/source my_env/bin/activate`

$ `export FLASK_APP=vooch.py`

$ `export FLASK_ENV=development`

$ `flask run`

### Deployment and hosting ⚙️
#### Deployed Site: 
#### Blog Article: 
#### LinkedIn: 

## Challenge

Problem Statement: The Portfolio Project aims to solve the challenge of visualizing Out of Home (OOH) artworks in real-world settings and obtaining instant feedback before printing. Traditionally, clients face difficulties in envisioning how their OOH advertisements will appear in various locations and understanding the potential impact on their target market. This project intends to provide a digital platform where clients can upload their approved OOH artworks, preview them in different settings, test them with their target audience, and receive valuable feedback, enabling informed decisions and optimizing the effectiveness of their OOH campaigns.
Limitations: While the Portfolio Project addresses the challenges of visualizing and testing OOH artworks, it does not handle the physical printing or implementation of the campaigns. The project's focus is on the digital visualization and feedback aspects, providing a virtual representation of the artworks in real-world scenarios. The actual printing and physical implementation of the OOH advertisements would require separate processes and logistics outside the scope of this project.
Target Audience and Users: The Portfolio Project aims to help clients involved in OOH advertising campaigns, such as advertisers, marketing agencies, and businesses seeking to promote their products or services through billboards, bus shelters, digital signage, and other OOH media. The users of the project would primarily include the clients themselves, who will upload and visualize their artworks, as well as conduct market testing to gather feedback. Additionally, the project might also cater to the target audience or market segment that is simulated during the testing phase, allowing them to provide feedback and insights on the OOH artworks.
Locale Dependency: The relevance of the Portfolio Project is not dependent on a specific locale. Out of Home (OOH) advertising is a global practice, and clients from various regions can benefit from the ability to visualize their artworks in different real-world settings. While specific locations may be selected within the app for visualizing the OOH artworks, the underlying concept and functionality of the project can be applied universally. The project can be adapted and customized to accommodate different regions, locations, and cultural contexts, making it relevant to a broad audience irrespective of locale.
In summary, the Portfolio Project addresses the challenge of visualizing and testing OOH artworks, empowering clients to make informed decisions and optimize the effectiveness of their campaigns. However, it does not handle the physical printing or implementation of the advertisements. The project will benefit clients involved in OOH advertising, and its relevance is not dependent on a specific locale as the concept can be applied globally.


## Risks
Technical Risks: 
a. Performance Issues: There is a risk of the application's performance being negatively impacted when handling a large number of uploaded artworks, visualizations, and user interactions. This could lead to slow loading times or unresponsiveness, affecting the user experience.
Safeguards and Alternatives: Implementing performance optimization techniques such as code and database optimization, caching mechanisms, and efficient image processing algorithms. Conducting load testing and performance profiling to identify and address bottlenecks. Considering server scalability options like load balancing and resource allocation
b. Compatibility Challenges: The application may encounter compatibility issues across different devices, browsers, or operating systems. Incompatibilities could result in visual discrepancies, functionality errors, or limited accessibility for users.
Safeguards/Alternatives: Conducting extensive cross-platform and cross-browser testing during development to ensure compatibility. Utilizing responsive design principles and frameworks to optimize the application's responsiveness across various devices and screen sizes. Adhering to web standards and best practices for increased compatibility.
Non-Technical Risks: 
a. Data Security and Privacy: There is a risk of unauthorized access to sensitive user data or artworks, potentially leading to breaches of privacy and data theft.
Strategies: Implementing robust security measures such as secure data transmission (HTTPS), data encryption, and authentication mechanisms. Adhering to industry-standard security practices, following OWASP guidelines, and conducting regular security audits and vulnerability assessments. Complying with relevant data protection regulations, such as GDPR or CCPA.
b. Legal and Copyright Issues: There may be a risk of inadvertently infringing on copyright or intellectual property rights when users upload and visualize artworks, especially if they are not the rightful owners.
Strategies: Incorporating user agreement and copyright disclaimer during the onboarding process to ensure users acknowledge their responsibility for the uploaded artworks. Implementing mechanisms to handle copyright claims or takedown requests promptly. Educating users about copyright laws and encouraging them to use only authorized or original artwork.
c. Market Feedback Reliability: While the project aims to provide simulated market feedback, there is a risk that the feedback may not fully represent real-world responses or accurately predict the success of OOH campaigns.
Strategies: Clearly communicating to users that simulated market feedback is an estimation and not a guarantee of real-world success. Encouraging users to interpret feedback as a valuable input rather than a definitive outcome. Continuously refining the feedback algorithms and simulation models based on real-world data and user feedback.
By proactively addressing technical risks through performance optimization, compatibility testing, and security measures and implementing strategies to prevent non-technical risks related to data security, copyright, and market feedback reliability, the Portfolio Project aims to minimize potential negative impacts and ensure a secure and reliable user experience. Regular monitoring, updates, and user feedback collection will be instrumental in identifying and addressing any emerging risks throughout the project's lifecycle.

## Authors

CLEVERS RUNGENE - Project Manager

LAWRENCE SAGINI


## Conclusion

VOOHC will be available to everyone in the OOH industry. Additionally, we will be adding functionality whereby the client can engage with their target market and get instant feedback regarding the creatives they are developing before they go live. This reduces the error rate.
