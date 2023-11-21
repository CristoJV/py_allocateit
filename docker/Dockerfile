# Dockerfile with support for GPU
# author: CristoJV
# date: 2023-11-16

FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

# --------------------------------------------------------------------------- #
# Preconfigure the timezone
# --------------------------------------------------------------------------- #
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata && \
    ln -fs /usr/share/zoneinfo/Europe/Madrid /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
    apt-get clean

# --------------------------------------------------------------------------- #
# Install the basic packages
# --------------------------------------------------------------------------- #
RUN apt update && \
    apt install --no-install-recommends -y gcc git zip curl htop \
    libgl1-mesa-glx libglib2.0-0 gnupg g++ build-essential \
    v4l-utils software-properties-common screen

# --------------------------------------------------------------------------- #
# Install Python
# --------------------------------------------------------------------------- #
ARG PYTHON_VERSION
RUN add-apt-repository ppa:deadsnakes/ppa && \
    apt update && \
    apt install -y python${PYTHON_VERSION} python${PYTHON_VERSION}-dev \
    python${PYTHON_VERSION}-distutils python3-tk python3-pip && \
    apt clean

# --------------------------------------------------------------------------- #
# Setup virtual environment
# --------------------------------------------------------------------------- #
ENV SHELL /bin/bash
SHELL ["/bin/bash", "-c"]

ARG VENV_PATH
RUN python${PYTHON_VERSION} -m pip install --upgrade pip && \
    python${PYTHON_VERSION} -m pip install setuptools && \
    python${PYTHON_VERSION} -m pip install virtualenv && \
    python${PYTHON_VERSION} -m virtualenv ${VENV_PATH} && \
    echo "source ${VENV_PATH}/bin/activate" >> ~/.bashrc

# --------------------------------------------------------------------------- #
# Install PyTorch
# --------------------------------------------------------------------------- #
ARG PYTORCH_VERSION
ARG TORCHVISION_VERSION
ARG TORCHAUDIO_VERSION
ARG CUDA_VERSION
RUN source ${VENV_PATH}/bin/activate && \
    pip install torch==${PYTORCH_VERSION}+cu${CUDA_VERSION} \
    torchvision==${TORCHVISION_VERSION}+cu${CUDA_VERSION} \
    torchaudio==${TORCHAUDIO_VERSION}+cu${CUDA_VERSION} \
    --index-url https://download.pytorch.org/whl/cu${CUDA_VERSION}

# --------------------------------------------------------------------------- #
# Install Python packages
# --------------------------------------------------------------------------- #
ARG REQUIREMENTS_PATH
COPY ${REQUIREMENTS_PATH}/requirements.txt /tmp/requirements.txt
COPY ${REQUIREMENTS_PATH}/requirements-dev.txt /tmp/requirements-dev.txt

RUN source ${VENV_PATH}/bin/activate && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

RUN source ${VENV_PATH}/bin/activate && \
    pip install -r /tmp/requirements-dev.txt && \
    rm /tmp/requirements-dev.txt


# --------------------------------------------------------------------------- #
# Setup working directory
# --------------------------------------------------------------------------- #
ARG WORKDIR
WORKDIR ${WORKDIR}

# --------------------------------------------------------------------------- #
# Setup user
# --------------------------------------------------------------------------- #
ARG USER
ARG UID
ARG GID

RUN if [ ${USER} != "root" ] && [ ${UID:-0} -ne 0 ] && [ ${GID:-0} -ne 0 ]; \
    then \
    groupadd -g ${GID} ${USER} && \
    useradd -m -u ${UID} -g ${GID} -s /bin/bash ${USER} && \
    chown -R ${USER}:${USER} ${WORKDIR} && \
    chown -R ${USER}:${USER} ${VENV_PATH} && \
    echo "${USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers; \
    fi

USER ${USER}

# --------------------------------------------------------------------------- #
# Entrypoint
# --------------------------------------------------------------------------- #
ARG ENTRYPOINT_PATH
COPY ${ENTRYPOINT_PATH}/entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]