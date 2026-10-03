# 24GHz mmWave Radar Integration with Raspberry Pi Pico for Motion Analysis

## Project Overview
This project demonstrates a real-time human motion detection system using a 24GHz RD-03D mmWave Radar integrated with a Raspberry Pi Pico. The radar detects human presence and motion without using a camera, making it suitable for privacy-preserving sensing applications. The processed data is sent to a PC through UART for real-time visualization and analysis.

## Features
- Human presence detection
- Motion detection
- Contactless sensing
- Real-time data processing
- UART communication
- Low-power embedded system
- Works in low-light and dusty environments
- Privacy-friendly (No camera required)

## Hardware Used
- RD-03D 24GHz mmWave Radar Module
- Raspberry Pi Pico
- USB Cable
- Personal Computer
- Jumper Wires
- 5V Power Supply

## Software Used
- MicroPython
- Thonny IDE
- UART Serial Communication

## Block Diagram

```
Human Target
      │
RD-03D Radar
      │ UART
Raspberry Pi Pico
      │ USB
      PC
```

## Working Principle
1. The RD-03D radar transmits 24GHz electromagnetic waves.
2. The reflected waves from a human are received by the radar.
3. The radar sends motion data to the Raspberry Pi Pico through UART.
4. The Pico processes the received data.
5. The processed information is transmitted to a PC.
6. The PC displays the motion data in real time.

## Applications
- Smart Home Automation
- Human Presence Detection
- Security Systems
- Occupancy Monitoring
- Healthcare Monitoring
- Industrial Automation

## Advantages
- Contactless detection
- High accuracy
- Low power consumption
- Privacy protection
- Reliable in low-light environments
- Compact and low-cost solution

## Future Enhancements
- Multi-person tracking
- AI-based motion classification
- IoT cloud integration
- Mobile application support
- Gesture recognition

## Repository Structure

```
24GHz-mmWave-Radar-Motion-Analysis
│── README.md
│── Report/
│── Source_Code/
│── Images/
│── Circuit_Diagram/
│── Output/
│── LICENSE
```

## Author

**Karthik G**  
Electronics and Communication Engineering (ECE)  
PES Institute of Technology and Management, Shivamogga
