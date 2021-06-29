MODEL=java-small
DATA_PATH=OJ_raw_pkl_test/OJ_raw_pkl_test.pkl
NODE_TYPE_VOCAB_PATH=vocab/type_vocab.csv
NODE_TOKEN_VOCAB_PATH=vocab/${MODEL}/token_vocab.csv
BATCH_SIZE=3
WORKER=4
CHECKPOINT_EVERY=300
TREE_SIZE_THRESHOLD_UPPER=2900
TREE_SIZE_THRESHOLD_LOWER=20
CUDA=-1
VALIDATING=1
NODE_TYPE_DIM=30
NODE_TOKEN_DIM=30
CONV_DIM=50
NUM_CONV=1
TASK=1
INCLUDE_TOKEN=1
EPOCH=20
PYTHON=python3
${PYTHON} infer.py \
--data_path ${DATA_PATH} \
--subtree_vocabulary_path --cuda ${CUDA} \
--batch_size ${BATCH_SIZE} --checkpoint_every ${CHECKPOINT_EVERY} \
--node_type_dim ${NODE_TYPE_DIM} --node_token_dim ${NODE_TOKEN_DIM} \
--num_conv ${NUM_CONV} \
--node_type_vocabulary_path ${NODE_TYPE_VOCAB_PATH} \
--token_vocabulary_path ${NODE_TOKEN_VOCAB_PATH} \
--task ${TASK} --epochs ${EPOCH} --worker ${WORKER} \
--include_token ${INCLUDE_TOKEN} --output_size ${CONV_DIM} --model ${MODEL} \
--tree_size_threshold_upper ${TREE_SIZE_THRESHOLD_UPPER} --tree_size_threshold_lower ${TREE_SIZE_THRESHOLD_LOWER}
