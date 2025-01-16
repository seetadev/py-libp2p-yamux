# Yamux for py-libp2p

## Introduction

Yamux (Yet Another Multiplexer) is a simple multiplexing protocol used to manage multiple streams over a single connection. This implementation integrates Yamux into the `py-libp2p` framework, allowing for efficient stream management within the `libp2p` network stack.

## Installation

To integrate Yamux with `py-libp2p`, follow these steps:

1. Clone the `py-libp2p` repository if you haven't already:

   ```bash
   git clone https://github.com/libp2p/py-libp2p.git
   cd py-libp2p
   ```

2. Copy the `yamux.py` and `yamux_transport.py` files into the `py-libp2p` project directory.

3. Install any necessary dependencies (if not already installed):

  

## Usage

### Setting Up Yamux Transport

1. Import and configure the Yamux transport in your `py-libp2p` application:

   ```python
   from yamux_transport import YamuxTransport
   from libp2p.transport.tcp.tcp import TCP

   base_transport = TCP()
   yamux_transport = YamuxTransport(base_transport)
   ```

2. Use `yamux_transport` for creating connections and listeners:

   ```python
   # Example of dialing a peer
   conn = await yamux_transport.dial(peer_id, endpoint)

   # Example of starting a listener
   listener = await yamux_transport.listen(endpoint)
   ``
   ```

## Testing

### Unit Tests

To run unit tests for the Yamux implementation:

1. Navigate to the directory containing `test_yamux.py`.
2. Run the tests using `unittest`:
   ```bash
   python -m unittest discover -s . -p "test_yamux.py"
   ```

### Integration Tests

To test the integration of Yamux with `py-libp2p`:

1. Write integration tests focusing on `py-libp2p` functionality with Yamux.
2. Execute the tests similarly to unit tests, ensuring all components work together correctly.

## Contributing

We welcome contributions to improve the Yamux implementation for `py-libp2p`. Please follow these guidelines:

1. Fork the repository and create your feature branch:

   ```bash
   git checkout -b feature/YourFeature
   ```

2. Commit your changes:

   ```bash
   git commit -m 'Add your feature'
   ```

3. Push to the branch:

   ```bash
   git push origin feature/YourFeature
   ```

4. Open a Pull Request, providing a detailed description of your changes.

## Reference

This implementation and documentation were inspired by the `ChainSafe/js-libp2p-yamux` project. For further understanding, you can refer to their [GitHub repository] (https://github.com/ChainSafe/js-libp2p-yamux).




