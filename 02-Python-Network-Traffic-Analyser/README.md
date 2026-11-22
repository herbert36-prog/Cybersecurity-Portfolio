# Python Network Traffic Analysis Tool for Mobile and IoT Devices

## Project Overview

This project involved designing and developing a lightweight Python-based network traffic analysis tool as part of my final-year Computer Science with Cybersecurity degree at Keele University.

The aim was to make network traffic easier to capture, explore and understand, particularly for users who may not have experience with professional network analysis software.

The application uses PyShark to capture live network packets, Pandas to process the collected information, and Streamlit and Plotly to present the results through an interactive dashboard.

The project focuses on making network traffic information more accessible by turning captured packet data into tables, statistics and visualisations.

## Problem Statement and Motivation

Network traffic analysis is an important part of understanding how devices communicate and identifying potentially unusual network behaviour.

Tools such as Wireshark provide detailed packet analysis capabilities, but their interfaces and large range of features can be difficult for beginners and non-technical users to understand.

This project explored whether a simpler Python-based application could provide a more accessible way to examine network traffic.

I was particularly interested in how mobile and Internet of Things (IoT) devices communicate across local networks and how network traffic information can help users understand their behaviour.

## Project Aim

To design and implement a lightweight Python-based network traffic analysis tool that provides clear and accessible visual insights into network behaviour.

## Project Objectives

The original project plan established four main objectives:

1. **Literature review:** Research existing network traffic analysis tools and identify usability limitations for non-technical users.
2. **Packet capture:** Design and implement a prototype capable of capturing and filtering network traffic.
3. **Dashboard development:** Develop an interactive dashboard using Streamlit and Plotly to visualise network traffic.
4. **Testing and evaluation:** Evaluate the usability and effectiveness of the tool within a small test network.

## Technologies and Tools

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| PyShark | Capturing live network packets |
| Wireshark / TShark | Packet capture engine used by PyShark |
| Pandas | Processing and organising captured data |
| Streamlit | Building the interactive dashboard |
| Plotly | Creating data visualisations |
| Visual Studio Code | Development environment |

## System Architecture

The application is divided into two main components.

### 1. Packet Capture – capture.py

The packet capture component uses PyShark to capture live network traffic through a selected network interface.

The captured packet information is processed and organised into structured data.

The current implementation records:

- Timestamp
- Protocol
- Packet length

The collected information is stored in a CSV file called `captured_data.csv`.

### 2. Data Visualisation – app.py

The dashboard component uses Streamlit to create an interactive interface.

It loads the captured CSV data using Pandas and presents the information in a format that is easier to explore.

Plotly is used to create visual representations of the network traffic.

### Application Workflow

1. Select the network interface for packet capture.
2. Capture live network packets using PyShark.
3. Extract relevant packet information.
4. Process the collected information.
5. Store the captured data in CSV format.
6. Load the CSV data into the Streamlit application.
7. Display network traffic information through tables, statistics and charts.

## Key Features

### Live Network Traffic Capture

Uses PyShark to capture packets from a selected network interface.

### Packet Data Processing

Uses Pandas to organise the captured information into a structured dataset.

### Protocol Analysis

Displays the different protocols found within the captured traffic and provides a visual breakdown of protocol frequency.

### Interactive Dashboard

Provides a Streamlit interface where users can explore the captured network traffic.

### Traffic Visualisation

Uses Plotly to present traffic information through charts, including protocol counts and traffic over time.

### Summary Statistics

Displays useful information about the captured dataset, including:

- Total number of packets.
- Number of unique protocols.
- Average packet size.
- Most frequently observed protocol.

## Network Security Relevance

Network traffic analysis can support cybersecurity monitoring by helping analysts understand communication patterns between devices.

For example, monitoring protocol distribution and changes in traffic volume can help highlight activity that may require further investigation.

This project provides an introductory way to explore these concepts through packet capture and visualisation.

However, the application does not currently perform automated threat detection or classify traffic as malicious. The visualisations are intended to support exploration and understanding of network behaviour.

## Implementation Challenges and Technical Considerations

During development, I worked with several technologies that needed to operate together.

One important consideration was configuring PyShark and its dependency on TShark, which is responsible for packet capture.

Another consideration was processing the captured packet information into a format that could be loaded and displayed by Streamlit.

The dashboard also required the data to be presented clearly so that users could understand the information without needing to examine every packet individually.

## Project Limitations

The current implementation has some limitations compared with the original project objectives.

- The captured dataset currently focuses on timestamps, protocols and packet lengths.
- Source and destination IP addresses are not currently included in the stored dataset.
- The application does not identify individual mobile or IoT devices.
- The dashboard provides visual analysis but does not automatically detect malicious traffic.
- The application has not been established as a production-grade network monitoring solution.

These limitations provide opportunities for further development.

## Future Improvements

Possible improvements include:

- Extracting source and destination IP addresses.
- Identifying and categorising individual network devices.
- Adding more detailed packet filtering options.
- Introducing detection rules for unusual network behaviour.
- Adding alerts for potentially suspicious traffic patterns.
- Supporting additional network traffic analysis features.
- Improving usability through further testing with non-technical users.

## Project Files

| File | Description |
|---|---|
| `capture.py` | Captures and processes live network packets. |
| `app.py` | Runs the Streamlit dashboard. |
| `requirements.txt` | Lists the required Python packages. |

## Video Demonstrations

Video demonstrations of the application will be added here.

## Skills Demonstrated

- Python programming.
- Network traffic analysis.
- Packet capture using PyShark.
- Understanding of network protocols.
- Data processing using Pandas.
- Interactive dashboard development.
- Data visualisation using Plotly.
- Troubleshooting and debugging.
- Technical documentation.

## Conclusion

This project gave me practical experience developing a Python-based network traffic analysis application.

It allowed me to combine programming, networking and data visualisation to create a tool that makes captured network information easier to understand.

Through the development process, I gained experience working with packet capture libraries, processing network data and building an interactive dashboard.

The project also developed my understanding of how network traffic analysis can contribute to cybersecurity monitoring and the importance of presenting technical information in an accessible way.

## Technical Challenges and Problem-Solving

One of the biggest challenges during this project was deciding how to approach the development of the network traffic analysis tool.

The research, planning and technical decision-making took approximately four months. During this period, I carried out independent research and discussed different approaches with my university supervisor before settling on the final implementation.

### Choosing the Right Programming Language

Initially, I needed to research which programming language would be most suitable for developing the application.

I considered the requirements of the project, particularly live packet capture, processing network data and presenting information through a visual dashboard.

After researching the available options, I decided to use Python. This allowed me to work with libraries such as PyShark, Pandas, Streamlit and Plotly within one application.

### Choosing Between PyShark and Python Sockets

Another important decision was how to capture network packets.

I researched two possible approaches:

- **PyShark:** A Python library that provides access to packet capture and analysis through Wireshark's TShark engine.
- **Python Sockets:** A lower-level approach that provides access to network communication and can be used to build packet-handling functionality.

I had to consider which approach was more appropriate for the requirements of my project.

I ultimately used PyShark because it provided an existing packet capture and analysis framework that I could integrate into my Python application.

This research helped me understand that different technologies can achieve similar objectives but offer different levels of functionality and complexity.

### Configuring Live Packet Capture

Getting PyShark working correctly was another challenge.

The application required the correct configuration of Wireshark/TShark and the Python environment. I also encountered issues relating to Python's asynchronous event loop when implementing live packet capture.

I had to investigate how the capture process worked, troubleshoot the configuration and make adjustments to get the packet capture functionality working.

This helped me develop my understanding of packet capture tools, Python libraries and troubleshooting.

### Data Privacy and Ethical Considerations

An important consideration throughout the project was making sure that network monitoring was carried out responsibly.

Network packets can contain sensitive information, particularly when monitoring devices used by other people.

I therefore had to consider what information the application actually needed to collect and how to avoid unnecessarily collecting personal information.

My project plan specified that testing would take place within my own local network using my own mobile phone and IoT devices. It also specified that the analysis would focus on packet metadata rather than collecting personal data.

The intended metadata included information such as source and destination IP addresses, protocol types, timestamps and packet sizes.

The implemented prototype currently stores timestamps, protocol information and packet lengths.

This experience helped me understand that developing a network monitoring tool involves more than making the technology work. It also requires considering privacy, responsible data collection and the potential impact of monitoring network activity.

### Working with My Supervisor

Throughout the planning and development process, I discussed the project with my university supervisor.

These discussions helped me consider different technical approaches, review my decisions and develop a clearer understanding of what was achievable within the project.

It also taught me the importance of researching a problem before committing to a particular technical solution.

## Personal Reflection

I spent approximately four months researching, planning and working through the technical decisions involved in this project.

At times, I found the process challenging because I was learning about unfamiliar technologies and had to decide which tools would be most appropriate for my application.

I particularly remember having to research the differences between PyShark and Python sockets before deciding how to approach packet capture. I also had to work through configuration issues when getting live packet capture working.

One of the things I took away from this project was the importance of not rushing into development. Spending time researching, discussing ideas with my supervisor and understanding the requirements helped me make more informed decisions.

I also became more aware of the privacy responsibilities involved in network monitoring. Before this project, I was mainly interested in understanding how devices communicate. During development, I realised that analysing network traffic also requires careful consideration of what information is collected and how it is handled.

Overall, this project improved my confidence in researching technical problems, comparing technologies and troubleshooting unfamiliar software. It also strengthened my interest in networking and cybersecurity, particularly understanding how network traffic can be used to monitor and investigate device behaviour.
## Video Demonstrations

The following videos demonstrate the Python Network Traffic Analysis Tool.

- **Demo 1:** [Watch Demo 1](https://www.youtube.com/watch?v=buFGn4FQDP0)
- **Demo 2:** [Watch Demo 2](https://youtu.be/wmuzJgJBdY8)
- **Demo 3:** [Watch Demo 3](https://youtu.be/zLSs6PzbTI4)
