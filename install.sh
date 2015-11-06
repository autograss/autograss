if [ -z "$1" ]; then
  echo "Usage: $0 <movementalgorithm path>"
fi

MOVEMENTAL_ALGORITHM_PATH=$1
MOVEMENTAL_ALGORITHM_NAME=${1##*/}

ln -s $MOVEMENTAL_ALGORITHM_PATH

$MOVEMENTAL_ALGORITHM_PATH/install_dependencies.sh
