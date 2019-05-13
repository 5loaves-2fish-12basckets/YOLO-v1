
import sys
sys.path.append('module')

from module.brother import Trainer 
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--modeltype', type=str, default='vgg',
                        help='vgg or res')
    parser.add_argument('--taskname', type=str, default='vgg',
                        help='taskname for model saving etc')
    parser.add_argument('--resum', type=str, default=None,
                        help='resume epoch')
    
    parser.add_argument('--data_dir', type=str, default='dataset')
    parser.add_argument('--epochs', type=int, default=100)
    parser.add_argument('--batch_size', type=int, default=16)
    parser.add_argument('--augmentation', type=bool, default=True)

    args = parser.parse_args()
    print('modeltype', args.modeltype, 'taskname', args.taskname, 'train epoch', args.epochs, 'batch_size', args.batch_size, 'aug', args.augmentation)
    trainer = Trainer(args)
    trainer.train()

if __name__ == '__main__':
    main()